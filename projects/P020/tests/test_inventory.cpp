#include <cassert>
#include <iostream>
#define TESTING
#include "../src/inventory.cpp"
int main(){
    Inventory inv;
    inv.add(std::make_unique<Item>("A",3));
    assert(inv.size()==1);
    assert(inv.find("A") && inv.find("A")->qty()==3);
    inv.find("A")->add(2);
    assert(inv.find("A")->qty()==5);
    assert(inv.find("X")==nullptr);
    bool dup=false; try{ inv.add(std::make_unique<Item>("A",1)); }catch(const std::invalid_argument&){dup=true;}
    assert(dup);
    std::cout<<"P020: RAII unique_ptr PASS\n";
}
