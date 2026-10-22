#include <cassert>
#include <limits>
#define TESTING
#include "../src/inventory.cpp"
int main() {
    Item item("A", std::numeric_limits<int>::max());
    bool overflow = false;
    try { item.add(1); } catch (const std::overflow_error&) { overflow = true; }
    assert(overflow);
    assert(item.qty() == std::numeric_limits<int>::max());
    item.add(0);
    assert(item.qty() == std::numeric_limits<int>::max());
}
