#include "ring_buffer.h"
#include <stdlib.h>
int rb_init(RingBuffer *rb, size_t capacity) {
    if (!rb || capacity == 0) return -1;
    rb->data = calloc(capacity, sizeof(int));
    if (!rb->data) return -1;
    rb->capacity=capacity; rb->head=rb->tail=rb->size=0; return 0;
}
void rb_free(RingBuffer *rb) { if (rb) { free(rb->data); rb->data=NULL; rb->capacity=rb->size=0; } }
int rb_push(RingBuffer *rb, int value) {
    if (!rb || !rb->data || rb->capacity == 0 || rb->size == rb->capacity) return -1;
    rb->data[rb->tail]=value; rb->tail=(rb->tail+1)%rb->capacity; rb->size++; return 0;
}
int rb_pop(RingBuffer *rb, int *value) {
    if (!rb || !rb->data || !value || rb->size==0) return -1;
    *value=rb->data[rb->head]; rb->head=(rb->head+1)%rb->capacity; rb->size--; return 0;
}
