#include <iostream>
#include <fstream>
#include <unordered_map>
#include <chrono>
#include <vector>
#include <algorithm>
#include <iomanip>

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

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();  // Record start time

    // Use std::unordered_map data structure
    std::unordered_map<std::string, int> filenameMap;

    // Read log file
    std::ifstream logFile("access_log");
    if (!logFile.is_open()) {
        std::cout << "Error opening file!" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(logFile, line)) {
        std::string filename = extractFilename(line);

        if (!filename.empty()) {
            // Increment count in std::unordered_map for all requests
            filenameMap[filename]++;
        }
    }
    logFile.close();

    // Calculate the top 10 most visited pages
    std::vector<std::pair<std::string, int>> sortedFilenames(filenameMap.begin(), filenameMap.end());

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
