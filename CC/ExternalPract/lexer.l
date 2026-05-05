%{
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int ignorecase_cmp(const char *a, const char *b) {
    while (*a && *b) { if (tolower((unsigned char)*a) != tolower((unsigned char)*b)) return 0; a++; b++; }
    return *a==0 && *b==0;
}
%}

%option noyywrap

%%
[\n\r]+    { ECHO; }
[ \t]+    { ECHO; }
.         { ECHO; }
%%

int main(int argc, char **argv) {
    if (argc<2) { fprintf(stderr, "Usage: text_processor <searchword>\n"); return 1; }
    char search[128]; strcpy(search, argv[1]);
    int c; char buf[4096]; int bi = 0;
    while ((c = getchar()) != EOF) {
        if (bi < (int)sizeof(buf)-1) buf[bi++] = (char)c;
    }
    buf[bi]=0;

    printf("\nHighlighted Output:\n");
    char out[8192]; int oi=0; int i=0; int count=0;
    while (buf[i]) {
        if (isalpha((unsigned char)buf[i]) || buf[i]=='_') {
            int j=i; char tok[256]; int tj=0;
            while (isalpha((unsigned char)buf[j]) || isdigit((unsigned char)buf[j]) || buf[j]=='_') tok[tj++]=buf[j++];
            tok[tj]=0;
            int match = 0;
            if (tj== (int)strlen(search)) {
                match = 1; for (int k=0;k<tj;k++) if (tolower((unsigned char)tok[k])!=tolower((unsigned char)search[k])) { match=0; break; }
            }
            if (match) {
                out[oi++]='['; for (int k=0;k<tj;k++) out[oi++]=tok[k]; out[oi++]=']'; count++;
            } else {
                for (int k=0;k<tj;k++) out[oi++]=tok[k];
            }
            i=j; continue;
        }
        out[oi++]=buf[i++];
    }
    out[oi]=0; printf("%s\n", out);

    int dec=0, inter=0, exc=0, total=0;
    char *p = buf; int sidx = 0;
    printf("\nAnalysis Output:\n");
    while (*p) {
        while (*p && isspace((unsigned char)*p)) p++;
        if (!*p) break;
        char sentence[1024]; int si=0; int found=0;
        while (*p) {
            sentence[si++]=*p;
            if (*p=='.' || *p=='?' || *p=='!') { found=1; p++; break; }
            p++;
        }
        sentence[si]=0;
        if (!found) break;
        total++;
        char last = sentence[si-1];
        if (last=='.') dec++; else if (last=='?') inter++; else if (last=='!') exc++;
        int k=0; while (sentence[k] && isspace((unsigned char)sentence[k])) k++;
        int valid = 0; if (sentence[k] && isupper((unsigned char)sentence[k])) valid = 1;
        printf("Sentence %d: %s\n", total, valid?"Valid":"Invalid - Sentence should start with capital letter");
    }
    printf("\nDeclarative Sentences: %d\nInterrogative Sentences: %d\nExclamatory Sentences: %d\nTotal Sentences: %d\n", dec, inter, exc, total);

    printf("\nRepeated Consecutive Words Found:\n");
    int foundrep = 0;
    char lasttok[256]="";
    i=0; while (buf[i]) {
        if (isalpha((unsigned char)buf[i]) || buf[i]=='_') {
            int j=i; char tok[256]; int tj=0;
            while (isalpha((unsigned char)buf[j]) || isdigit((unsigned char)buf[j]) || buf[j]=='_') tok[tj++]=buf[j++]; tok[tj]=0;
            if (tj>0 && lasttok[0]) {
                int same=1; if (tj!=(int)strlen(lasttok)) same=0; else for (int k=0;k<tj;k++) if (tolower((unsigned char)tok[k])!=tolower((unsigned char)lasttok[k])) { same=0; break; }
                if (same) { printf("%s %s\n", lasttok, tok); foundrep=1; }
            }
            strcpy(lasttok, tok);
            i=j; continue;
        }
        if (!isspace((unsigned char)buf[i])) { lasttok[0]=0; }
        i++;
    }
    if (!foundrep) printf("None\n");

    printf("\nSearch Word Occurrences: %d\n", count);

    return 0;
}
