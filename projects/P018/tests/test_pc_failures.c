#include <assert.h>
#include <errno.h>
#include <pthread.h>
#define TESTING
#include "../src/producer_consumer.c"
static int stage, condition_calls, create_calls;
int __real_pthread_mutex_init(pthread_mutex_t*, const pthread_mutexattr_t*);
int __real_pthread_cond_init(pthread_cond_t*, const pthread_condattr_t*);
int __real_pthread_create(pthread_t*, const pthread_attr_t*, void *(*)(void*), void*);
int __wrap_pthread_mutex_init(pthread_mutex_t *m, const pthread_mutexattr_t *a) {
    return stage==1 ? EAGAIN : __real_pthread_mutex_init(m,a);
}
int __wrap_pthread_cond_init(pthread_cond_t *c, const pthread_condattr_t *a) {
    condition_calls++;
    if ((stage==2 && condition_calls==1) || (stage==3 && condition_calls==2)) return EAGAIN;
    return __real_pthread_cond_init(c,a);
}
int __wrap_pthread_create(pthread_t *t, const pthread_attr_t *a, void *(*fn)(void*), void *v) {
    create_calls++;
    if ((stage==4 && create_calls==1) || (stage==5 && create_calls==2)) return EAGAIN;
    return __real_pthread_create(t,a,fn,v);
}
int main(void) {
    assert(run_demo(NULL)==-1);
    for (stage=1;stage<=5;stage++) {
        condition_calls=create_calls=0;long sum=123;
        assert(run_demo(&sum)==-1);assert(sum==123);
    }
    stage=0;condition_calls=create_calls=0;long sum=0;
    assert(run_demo(&sum)==0 && sum==5050);
}
