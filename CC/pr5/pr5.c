#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 10

char prod[MAX][MAX], first[MAX][MAX], follow[MAX][MAX];
char nt[MAX];
int n, ntc = 0;

int isNT(char c) { return isupper(c); }

void add(char s[], char c) {
    if (!strchr(s, c)) {
        int l = strlen(s);
        s[l] = c;
        s[l+1] = '\0';
    }
}

int indexOf(char c) {
    for (int i = 0; i < ntc; i++)
        if (nt[i] == c) return i;
    return -1;
}

void findFirst(char c) {
    int idx = indexOf(c);

    for (int i = 0; i < n; i++) {
        if (prod[i][0] == c) {
            char *rhs = &prod[i][2];

            if (!isNT(rhs[0])) {
                add(first[idx], rhs[0]);
            } else {
                int j = 0;
                while (rhs[j]) {
                    int id = indexOf(rhs[j]);
                    if (id == -1) break;

                    findFirst(rhs[j]);

                    for (int k = 0; first[id][k]; k++)
                        if (first[id][k] != '#')
                            add(first[idx], first[id][k]);

                    if (!strchr(first[id], '#'))
                        break;

                    j++;
                    if (!rhs[j])
                        add(first[idx], '#');
                }
            }
        }
    }
}

void findFollow(char c) {
    int idx = indexOf(c);

    if (idx == 0) add(follow[idx], '$');

    for (int i = 0; i < n; i++) {
        char *rhs = &prod[i][2];

        for (int j = 0; rhs[j]; j++) {
            if (rhs[j] == c) {

                if (rhs[j+1]) {
                    if (!isNT(rhs[j+1])) {
                        add(follow[idx], rhs[j+1]);
                    } else {
                        int id = indexOf(rhs[j+1]);
                        findFirst(rhs[j+1]);

                        for (int k = 0; first[id][k]; k++)
                            if (first[id][k] != '#')
                                add(follow[idx], first[id][k]);

                        if (strchr(first[id], '#'))
                            add(follow[idx], '$');
                    }
                } else {
                    int id = indexOf(prod[i][0]);
                    if (id != idx) {
                        findFollow(prod[i][0]);
                        for (int k = 0; follow[id][k]; k++)
                            add(follow[idx], follow[id][k]);
                    }
                }
            }
        }
    }
}

int main() {
    printf("Enter number of productions: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%s", prod[i]);
        if (indexOf(prod[i][0]) == -1)
            nt[ntc++] = prod[i][0];
    }

    for (int i = 0; i < ntc; i++)
        findFirst(nt[i]);

    for (int i = 0; i < ntc; i++)
        findFollow(nt[i]);

    printf("\nNT\tFIRST\tFOLLOW\n");
    for (int i = 0; i < ntc; i++)
        printf("%c\t{%s}\t{%s}\n", nt[i], first[i], follow[i]);

    return 0;
}
