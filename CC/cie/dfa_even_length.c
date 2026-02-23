#include <stdbool.h>
#include <stdio.h>
#include <string.h>

static bool is_even_length_binary(const char *s) {
    size_t len = strlen(s);
    for (size_t i = 0; i < len; i++) {
        if (s[i] != '0' && s[i] != '1') {
            return false;
        }
    }
    return (len % 2) == 0;
}

int main(void) {
    char input[1024];

    printf("Enter a binary string: ");
    if (!fgets(input, sizeof(input), stdin)) {
        return 1;
    }

    size_t len = strlen(input);
    if (len > 0 && input[len - 1] == '\n') {
        input[len - 1] = '\0';
    }

    if (is_even_length_binary(input)) {
        printf("Accepted (even length).\n");
    } else {
        printf("Rejected.\n");
    }

    return 0;
}
