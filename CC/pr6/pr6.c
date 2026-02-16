#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 20

char grammar[MAX][MAX], first[MAX][MAX], follow[MAX][MAX];
char table[MAX][MAX][MAX];  // Parsing table [non-terminal][terminal]
char terminals[MAX], nonTerminals[MAX];
int n, conflict = 0;

int contains(char *s, char c) {
    for (int i = 0; s[i]; i++) if (s[i] == c) return 1;
    return 0;
}

void add(char *s, char c) {
    if (!contains(s, c)) { int l = strlen(s); s[l] = c; s[l+1] = '\0'; }
}

int isNT(char c) { return isupper(c); }

void FIRST(char c);

void FIRST_str(char *str, char *res) {
    if (!str[0]) { add(res, '#'); return; }
    for (int i = 0; str[i]; i++) {
        if (!isNT(str[i])) { add(res, str[i]); return; }
        FIRST(str[i]);
        int idx = str[i] - 'A';
        for (int j = 0; first[idx][j]; j++)
            if (first[idx][j] != '#') add(res, first[idx][j]);
        if (!contains(first[idx], '#')) return;
    }
    add(res, '#');
}

void FIRST(char c) {
    int idx = c - 'A';
    if (first[idx][0]) return;
    for (int i = 0; i < n; i++) {
        if (grammar[i][0] == c) {
            char res[MAX] = "";
            FIRST_str(&grammar[i][3], res);
            for (int k = 0; res[k]; k++) add(first[idx], res[k]);
        }
    }
}

void FOLLOW(char c) {
    int idx = c - 'A';
    if (follow[idx][0]) return;
    if (c == grammar[0][0]) add(follow[idx], '$');
    
    for (int i = 0; i < n; i++) {
        for (int j = 3; grammar[i][j]; j++) {
            if (grammar[i][j] == c) {
                if (!grammar[i][j+1]) {
                    FOLLOW(grammar[i][0]);
                    int p = grammar[i][0] - 'A';
                    for (int k = 0; follow[p][k]; k++) add(follow[idx], follow[p][k]);
                } else {
                    char temp[MAX] = "";
                    FIRST_str(&grammar[i][j+1], temp);
                    for (int k = 0; temp[k]; k++)
                        if (temp[k] != '#') add(follow[idx], temp[k]);
                    if (contains(temp, '#')) {
                        FOLLOW(grammar[i][0]);
                        int p = grammar[i][0] - 'A';
                        for (int k = 0; follow[p][k]; k++) add(follow[idx], follow[p][k]);
                    }
                }
            }
        }
    }
}

void buildTable() {

    memset(table, 0, sizeof(table));
    strcpy(terminals, "");
    strcpy(nonTerminals, "");
    
    for (int i = 0; i < n; i++) {
        add(nonTerminals, grammar[i][0]);
        for (int j = 3; grammar[i][j]; j++)
            if (!isNT(grammar[i][j]) && grammar[i][j] != '#')
                add(terminals, grammar[i][j]);
    }
    add(terminals, '$');
    

    for (int i = 0; i < n; i++) {
        char A = grammar[i][0];
        int nt_idx = A - 'A';
        char temp[MAX] = "";
        FIRST_str(&grammar[i][3], temp);
        
        for (int j = 0; temp[j]; j++) {
            if (temp[j] != '#') {
                int t_idx = 0;
                for (int k = 0; terminals[k]; k++) {
                    if (terminals[k] == temp[j]) { t_idx = k; break; }
                }
                if (table[nt_idx][t_idx][0]) {
                    printf("CONFLICT at [%c,%c]: %s vs %s\n", A, temp[j], 
                           table[nt_idx][t_idx], &grammar[i][3]);
                    conflict = 1;
                }
                strcpy(table[nt_idx][t_idx], &grammar[i][3]);
            }
        }
        
        if (contains(temp, '#')) {
            int fol_idx = A - 'A';
            for (int j = 0; follow[fol_idx][j]; j++) {
                int t_idx = 0;
                for (int k = 0; terminals[k]; k++) {
                    if (terminals[k] == follow[fol_idx][j]) { t_idx = k; break; }
                }
                if (table[nt_idx][t_idx][0]) {
                    printf("CONFLICT at [%c,%c]: %s vs %s\n", A, follow[fol_idx][j],
                           table[nt_idx][t_idx], &grammar[i][3]);
                    conflict = 1;
                }
                strcpy(table[nt_idx][t_idx], &grammar[i][3]);
            }
        }
    }
}

void printTable() {
    printf("\n PREDICTIVE PARSING TABLE \n");
    printf("%-5s", "NT\\T");
    for (int i = 0; terminals[i]; i++) printf("%-8c", terminals[i]);
    printf("\n");
    
    for (int i = 0; nonTerminals[i]; i++) {
        printf("%-5c", nonTerminals[i]);
        int nt_idx = nonTerminals[i] - 'A';
        for (int j = 0; terminals[j]; j++) {
            if (table[nt_idx][j][0])
                printf("%-8s", table[nt_idx][j]);
            else
                printf("%-8s", "-");
        }
        printf("\n");
    }
}

int main() {
    printf("Enter number of productions: ");
    scanf("%d", &n);
    printf("Enter productions (format: A->alpha, use # for epsilon):\n");
    for (int i = 0; i < n; i++) {
        printf("%d: ", i+1);
        scanf("%s", grammar[i]);
    }
    
    
    memset(first, 0, sizeof(first));
    memset(follow, 0, sizeof(follow));
    
        for (int i = 0; i < n; i++) FIRST(grammar[i][0]);
    
        for (int i = 0; i < n; i++) FOLLOW(grammar[i][0]);
    
    
    printf("\n FIRST SETS \n");
    for (int i = 0; i < 26; i++) {
        if (first[i][0]) {
            printf("FIRST(%c) = { ", i+'A');
            for (int j = 0; first[i][j]; j++)
                printf("%c%s", first[i][j]=='#'?'E':first[i][j], first[i][j+1]?", ":"");
            printf(" }\n");
        }
    }
    
    printf("\n FOLLOW SETS \n");
    for (int i = 0; i < 26; i++) {
        if (follow[i][0]) {
            printf("FOLLOW(%c) = { ", i+'A');
            for (int j = 0; follow[i][j]; j++)
                printf("%c%s", follow[i][j], follow[i][j+1]?", ":"");
            printf(" }\n");
        }
    }
    
    
    buildTable();
    printTable();
    
    
    printf("\n LL(1) VALIDATION \n");
    if (conflict) {
        printf("Grammar is NOT LL(1) - Conflicts detected!\n");
        printf("Conflict Types:\n");
        printf("FIRST-FIRST: Multiple productions with same terminal in FIRST\n");
        printf("FIRST-FOLLOW: Epsilon production conflicts with FOLLOW symbols\n");
    } else {
        printf("Grammar is LL(1) - No conflicts!\n");
    }
    
    return 0;
}
