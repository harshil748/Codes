#include <stdbool.h>
#include <stdio.h>
#include <string.h>

static bool contains_ab(const char *s) {
    bool seen_a = false;

    for (size_t i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'a') {
            seen_a = true;
        } else if (s[i] == 'b') {
            if (seen_a) {
                return true;
            }
        } else {
            return false;
        }
    }

    return false;
}

int main(void) {
    char input[1024];

    printf("Enter a string over {a,b}: ");
    if (!fgets(input, sizeof(input), stdin)) {
        return 1;
    }

    size_t len = strlen(input);
    if (len > 0 && input[len - 1] == '\n') {
        input[len - 1] = '\0';
    }

    if (contains_ab(input)) {
        printf("Accepted (contains \"ab\").\n");
    } else {
        printf("Rejected.\n");
    }

    return 0;
}
