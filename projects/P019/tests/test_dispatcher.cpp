#include <cassert>
#include <iostream>
#define TESTING
#include "../src/dispatcher.cpp"
int main(){
    Dispatcher d;
    d.add(3,"A"); d.add(1,"B"); d.add(1,"C"); d.add(2,"D");
    assert(d.next().description=="B");
    assert(d.next().description=="C");
    assert(d.next().description=="D");
    assert(d.next().description=="A");
    bool bad=false; try{ d.add(9,"x"); } catch(const std::invalid_argument&){ bad=true; }
    assert(bad);
    std::cout<<"P019: priority_queue PASS\n";
}
