#include <memory>
#include <string>
#include <vector>
#include <stdexcept>
#include <limits>

class Item {
    std::string sku_;
    int qty_;
public:
    Item(std::string sku,int qty):sku_(std::move(sku)),qty_(qty){ if(qty<0) throw std::invalid_argument("qty"); }
    const std::string& sku() const { return sku_; }
    int qty() const { return qty_; }
    void add(int n){
        if(n<0) throw std::invalid_argument("n");
        if(n>std::numeric_limits<int>::max()-qty_) throw std::overflow_error("qty overflow");
        qty_+=n;
    }
};
class Inventory {
    std::vector<std::unique_ptr<Item>> items_;
public:
    void add(std::unique_ptr<Item> item){
        if(!item) throw std::invalid_argument("null");
        for(auto& p:items_) if(p->sku()==item->sku()) throw std::invalid_argument("duplicate");
        items_.push_back(std::move(item));
    }
    Item* find(const std::string& sku){
        for(auto& p:items_) if(p->sku()==sku) return p.get();
        return nullptr;
    }
    std::size_t size() const { return items_.size(); }
};
#ifndef TESTING
#include <iostream>
int main(){ Inventory i; i.add(std::make_unique<Item>("A",3)); std::cout<<i.size()<<"\n"; }
#endif
