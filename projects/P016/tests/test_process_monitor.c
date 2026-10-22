#include <assert.h>
#include <stdio.h>
#include <unistd.h>
#define TESTING
#include "../src/process_monitor.c"

int main(void) {
    ProcessInfo info;
    assert(read_process_info(getpid(), &info) == 0);
    assert(info.name[0] != '\0');
    assert(read_process_info(999999, &info) == -1);
    printf("P016: /proc parsing PASS; current process=%s\n", info.name);
    return 0;
}
