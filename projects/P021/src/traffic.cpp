#include <algorithm>
#include <vector>
#include <stdexcept>
#include <iostream>
struct Car { int arrival; int service; };
struct Result { int completed; double avgWait; };
Result simulate(const std::vector<Car>& input, int horizon) {
    if (horizon < 0) throw std::invalid_argument("horizon");
    auto cars = input;
    for (auto c : cars)
        if (c.arrival < 0 || c.service <= 0)
            throw std::invalid_argument("car");
    std::stable_sort(cars.begin(), cars.end(),
        [](const Car& a, const Car& b) { return a.arrival < b.arrival; });
    long long freeAt = 0, totalWait = 0;
    int completed = 0;
    for (auto c : cars) {
        long long start = std::max<long long>(c.arrival, freeAt);
        long long end = start + c.service;
        if (end > horizon) break;
        totalWait += start - c.arrival;
        freeAt = end;
        ++completed;
    }
    return {completed, completed ? double(totalWait)/completed : 0.0};
}
#ifndef TESTING
int main() {
    auto r = simulate({{0,2},{1,2},{3,1}},20);
    std::cout << r.completed << " " << r.avgWait << "\n";
}
#endif
