#include <queue>
#include <string>
#include <vector>
#include <stdexcept>

struct Emergency {
    int priority;          // 1 = massima
    long sequence;
    std::string description;
};
struct Compare {
    bool operator()(const Emergency& a, const Emergency& b) const {
        if (a.priority != b.priority) return a.priority > b.priority;
        return a.sequence > b.sequence;
    }
};
class Dispatcher {
    std::priority_queue<Emergency,std::vector<Emergency>,Compare> q;
    long seq=0;
public:
    void add(int priority, std::string text){
        if(priority<1 || priority>5) throw std::invalid_argument("priorita");
        q.push(Emergency{priority,seq++,std::move(text)});
    }
    Emergency next(){
        if(q.empty()) throw std::runtime_error("coda vuota");
        auto e=q.top(); q.pop(); return e;
    }
    bool empty() const { return q.empty(); }
};
#ifndef TESTING
#include <iostream>
int main(){ Dispatcher d; d.add(2,"guasto"); d.add(1,"emergenza"); std::cout<<d.next().description<<"\n"; }
#endif
