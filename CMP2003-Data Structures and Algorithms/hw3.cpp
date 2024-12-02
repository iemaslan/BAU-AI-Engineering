#include <iostream>
#include <fstream>
#include <unordered_map>
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
    return ""; 
}

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();  
    const int TABLE_SIZE = 1000; 

    class HashTable {
    private:
        struct Node {
            std::string key;
            int value;
            Node* next;

            Node(const std::string& k, int v) : key(k), value(v), next(nullptr) {}
        };

        mutable std::vector<Node*> table;

        int hashFunc(const std::string& key) const {
            unsigned int hash = 5381;
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
                    current->value++;  
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

        ~HashTable() {
            for (Node*& node : table) {
                while (node != nullptr) {
                    Node* temp = node;
                    node = node->next;
                    delete temp;
                }
                node = nullptr; 
            }
        }
    };

  
    std::unordered_map<std::string, int> filenameMap;

    
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
            
            hashTable.insertOrUpdate(filename);

            
            filenameMap[filename]++;
        }
    }
    logFile.close();

  
    std::vector<std::pair<std::string, int>> sortedFilenames(filenameMap.begin(), filenameMap.end());

   
    std::sort(sortedFilenames.begin(), sortedFilenames.end(),
              [](const std::pair<std::string, int>& a, const std::pair<std::string, int>& b) {
                  return a.second > b.second;
              });

    
    std::cout << std::left << std::setw(20) << "Filename" << std::setw(15) << "# of total visits" << std::endl;
    for (int i = 0; i < std::min(10, static_cast<int>(sortedFilenames.size())); ++i) {
        std::cout << std::setw(20) << sortedFilenames[i].first << std::setw(15) << sortedFilenames[i].second << std::endl;
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();
    std::cout << "\nTotal Elapsed Time: " << elapsed_time << " milliseconds" << std::endl;

    return 0;
}
