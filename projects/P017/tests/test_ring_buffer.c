#include <assert.h>
#include <stdio.h>
#include "../src/ring_buffer.h"
int main(void){
    RingBuffer rb; int x;
    assert(rb_init(&rb,3)==0);
    assert(rb_pop(&rb,&x)==-1);
    assert(rb_push(&rb,10)==0);
    assert(rb_push(&rb,20)==0);
    assert(rb_push(&rb,30)==0);
    assert(rb_push(&rb,40)==-1);
    assert(rb_pop(&rb,&x)==0 && x==10);
    assert(rb_push(&rb,40)==0);
    assert(rb_pop(&rb,&x)==0 && x==20);
    assert(rb_pop(&rb,&x)==0 && x==30);
    assert(rb_pop(&rb,&x)==0 && x==40);
    rb_free(&rb);
    puts("P017: ring buffer PASS");
    return 0;
}
