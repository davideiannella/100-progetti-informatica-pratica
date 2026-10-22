#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define CAP 8
#define N 100

typedef struct {
    int buf[CAP], head, tail, count;
    pthread_mutex_t m;
    pthread_cond_t not_empty, not_full;
    long sum;
} Shared;

void *producer(void *arg){
    Shared *s=arg;
    for(int x=1;x<=N;x++){
        pthread_mutex_lock(&s->m);
        while(s->count==CAP) pthread_cond_wait(&s->not_full,&s->m);
        s->buf[s->tail]=x; s->tail=(s->tail+1)%CAP; s->count++;
        pthread_cond_signal(&s->not_empty);
        pthread_mutex_unlock(&s->m);
    }
    return NULL;
}
void *consumer(void *arg){
    Shared *s=arg;
    for(int i=0;i<N;i++){
        pthread_mutex_lock(&s->m);
        while(s->count==0) pthread_cond_wait(&s->not_empty,&s->m);
        int x=s->buf[s->head]; s->head=(s->head+1)%CAP; s->count--;
        s->sum += x;
        pthread_cond_signal(&s->not_full);
        pthread_mutex_unlock(&s->m);
    }
    return NULL;
}
int run_demo(long *sum){
    if (!sum) return -1;
    Shared s={0};
    if (pthread_mutex_init(&s.m,NULL)!=0) return -1;
    if (pthread_cond_init(&s.not_empty,NULL)!=0) { pthread_mutex_destroy(&s.m); return -1; }
    if (pthread_cond_init(&s.not_full,NULL)!=0) { pthread_cond_destroy(&s.not_empty); pthread_mutex_destroy(&s.m); return -1; }
    pthread_t p,c;
    if(pthread_create(&p,NULL,producer,&s)!=0) {
        pthread_cond_destroy(&s.not_full); pthread_cond_destroy(&s.not_empty); pthread_mutex_destroy(&s.m); return -1;
    }
    if(pthread_create(&c,NULL,consumer,&s)!=0) { consumer(&s); pthread_join(p,NULL);
        pthread_mutex_destroy(&s.m); pthread_cond_destroy(&s.not_empty); pthread_cond_destroy(&s.not_full); return -1; }
    pthread_join(p,NULL); pthread_join(c,NULL);
    *sum=s.sum;
    pthread_mutex_destroy(&s.m); pthread_cond_destroy(&s.not_empty); pthread_cond_destroy(&s.not_full);
    return 0;
}
#ifndef TESTING
int main(void){ long sum; if(run_demo(&sum)!=0) return 1; printf("sum=%ld\n",sum); return 0; }
#endif
