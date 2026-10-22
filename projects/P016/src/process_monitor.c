#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <limits.h>

typedef struct {
    char name[256];
    long vm_rss_kb;
} ProcessInfo;

int read_process_info(pid_t pid, ProcessInfo *out) {
    char path[128], line[512];
    if (!out || pid <= 0) return -1;
    if (pid == getpid()) snprintf(path, sizeof(path), "/proc/self/status");
    else snprintf(path, sizeof(path), "/proc/%d/status", (int)pid);
    FILE *f = fopen(path, "r");
    if (!f) return -1;
    out->name[0] = '\0';
    out->vm_rss_kb = -1;
    while (fgets(line, sizeof(line), f)) {
        if (strncmp(line, "Name:", 5) == 0) {
            sscanf(line + 5, " %255[^\n]", out->name);
        } else if (strncmp(line, "VmRSS:", 6) == 0) {
            sscanf(line + 6, "%ld", &out->vm_rss_kb);
        }
    }
    fclose(f);
    return out->name[0] ? 0 : -1;
}

#ifndef TESTING
int main(int argc, char **argv) {
    pid_t pid = getpid();
    if (argc > 2) { fprintf(stderr, "Uso: monitor [PID]\n"); return 2; }
    if (argc == 2) {
        char *end;
        errno = 0;
        long value = strtol(argv[1], &end, 10);
        if (errno || end == argv[1] || *end || value <= 0 || value > INT_MAX) {
            fprintf(stderr, "PID non valido\n"); return 2;
        }
        pid = (pid_t)value;
    }
    ProcessInfo info;
    if (read_process_info(pid, &info) != 0) {
        fprintf(stderr, "Impossibile leggere PID %d\n", (int)pid);
        return 1;
    }
    printf("PID=%d Name=%s VmRSS=%ld kB\n", (int)pid, info.name, info.vm_rss_kb);
    return 0;
}
#endif
