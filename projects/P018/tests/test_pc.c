#include <assert.h>
#include <stdio.h>
#define TESTING
#include "../src/producer_consumer.c"
int main(void){
    long sum=0;
    assert(run_demo(&sum)==0);
    assert(sum == (100L*101L)/2L);
    printf("P018: producer-consumer PASS; sum=%ld\n",sum);
    return 0;
}
