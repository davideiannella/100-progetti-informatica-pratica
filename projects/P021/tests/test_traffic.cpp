#include <cassert>
#include <cmath>
#include <iostream>
#define TESTING
#include "../src/traffic.cpp"
int main(){
    auto r=simulate({{0,2},{1,2},{3,1}},20);
    assert(r.completed==3);
    assert(std::fabs(r.avgWait - (0+1+1)/3.0) < 1e-9);
    auto empty=simulate({},10);
    assert(empty.completed==0 && empty.avgWait==0);
    bool bad=false; try{ simulate({{-1,2}},10); }catch(const std::invalid_argument&){bad=true;}
    assert(bad);
    std::cout<<"P021: traffic simulation PASS; avgWait="<<r.avgWait<<"\n";
}
