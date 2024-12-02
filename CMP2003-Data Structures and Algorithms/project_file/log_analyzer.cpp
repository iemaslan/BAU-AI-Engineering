#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <sstream>

std::string extractFilename(const std::string& line) {
    size_t getPos = line.find("GET ");
    if (getPos != std::string::npos) {
        size_t spacePos = line.find_first_of(" ", getPos + 4);
        if (spacePos != std::string::npos) {
            return line.substr(getPos + 4, spacePos - getPos - 4);
        }
    }
    return ""; // If not found or invalid format
}

class HashTable {
private:
    struct Node {
        std::string key;
        int value;
        Node* next;

        Node(const std::string& k, int v) : key(k), value(v), next(nullptr) {}
    };

    const int TABLE_SIZE = 1000; // Define TABLE_SIZE as a member variable

    mutable std::vector<Node*> table;

    int hashFunc(const std::string& key) const {
        unsigned int hash = 5381; // Initial value
        for (char c : key) {
            hash = ((hash << 5) + hash) + static_cast<unsigned int>(c);
        }
        return hash % TABLE_SIZE;
    }

public:
    HashTable() : table(TABLE_SIZE, nullptr) {}

    void insertOrUpdate(const std::string& filename) const {
        int index = hashFunc(filename);

        if (table[index] == nullptr) {
            table[index] = new Node(filename, 1);
        } else {
            Node* current = table[index];
            while (current->next != nullptr && current->key != filename) {
                current = current->next;
            }

            if (current->key == filename) {
                current->value++;  // Increment the count for an existing filename
            } else {
                current->next = new Node(filename, 1);
            }
        }
    }

    int getCount(const std::string& filename) const {
        int index = hashFunc(filename);

        Node* current = table[index];
        while (current != nullptr) {
            if (current->key == filename) {
                return current->value;
            }
            current = current->next;
        }

        return 0;
    }

    const std::vector<Node*>& getTable() const {
        return table;
    }

    // Public Node struct definition
    struct PublicNode {
        std::string key;
        int value;

        PublicNode(const std::string& k, int v) : key(k), value(v) {}
    };

    // Public function to get the nodes in the linked list
    const std::vector<PublicNode> getNodes(int index) const {
        const Node* current = table[index];
        std::vector<PublicNode> publicNodes;

        while (current != nullptr) {
            publicNodes.emplace_back(current->key, current->value);
            current = current->next;
        }

        return publicNodes;
    }

    ~HashTable() {
        for (Node*& node : table) {
            while (node != nullptr) {
                Node* temp = node;
                node = node->next;
                delete temp;
            }
            node = nullptr; // Set the element to nullptr after deleting all nodes
        }
    }
};

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();  // Record start time

    // Read log file
    std::ifstream logFile("access_log");
    if (!logFile.is_open()) {
        std::cout << "Error opening file!" << std::endl;
        return 1;
    }

    HashTable hashTable;

    std::string line;
    while (std::getline(logFile, line)) {
        std::string filename = extractFilename(line);

        if (!filename.empty()) {
            // Increment count in your hash table for all requests
            hashTable.insertOrUpdate(filename);
        }
    }
    logFile.close();

    // Create a vector to store the data for sorting
    std::vector<std::pair<std::string, int>> sortedFilenames;

    // Iterate through the hash table and populate the vector
    for (int i = 0; i < hashTable.getTable().size(); ++i) {
        const std::vector<HashTable::PublicNode> nodes = hashTable.getNodes(i);
        for (const auto& node : nodes) {
            sortedFilenames.emplace_back(node.key, node.value);
        }
    }

    // Sort the vector in descending order
    std::sort(sortedFilenames.begin(), sortedFilenames.end(),
              [](const std::pair<std::string, int>& a, const std::pair<std::string, int>& b) {
                  return a.second > b.second; // Sort by visit count in descending order
              });

    // Output the top 10 most visited pages
    std::cout << std::left << std::setw(20) << "Filename" << std::setw(15) << "# of total visits" << std::endl;
    for (int i = 0; i < std::min(10, static_cast<int>(sortedFilenames.size())); ++i) {
        std::cout << std::setw(20) << sortedFilenames[i].first << std::setw(15) << sortedFilenames[i].second << std::endl;
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();
    std::cout << "\nTotal Elapsed Time: " << elapsed_time << " milliseconds" << std::endl;

    return 0;
}
