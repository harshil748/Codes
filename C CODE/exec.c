#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
 int f_return;
    f_return = fork();  
    if (f_return < 0) {
        perror("Fork failed");
        exit(1);
    } else if (f_return == 0) {
        printf("This is a child process.\n");
        execlp("./arith", "arith", NULL);
        perror("execlp failed");
        exit(1);
    } else {
        printf("Parent starts execution.\n");
        wait(NULL);
    }
    return 0;
}