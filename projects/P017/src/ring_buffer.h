#ifndef RING_BUFFER_H
#define RING_BUFFER_H
#include <stddef.h>
typedef struct { int *data; size_t capacity, head, tail, size; } RingBuffer;
int rb_init(RingBuffer *rb, size_t capacity);
void rb_free(RingBuffer *rb);
int rb_push(RingBuffer *rb, int value);
int rb_pop(RingBuffer *rb, int *value);
#endif
