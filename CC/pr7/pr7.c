#include <stdio.h>
#include <string.h>

#define MAX 20

typedef struct{int p,d;}Item;
typedef struct{Item it[MAX];int n;}State;

char prodL[]={'Z','S','A','A'};
char *prodR[]={"S","AA","aA","b"};
int prodN=4;

State st[MAX];
int stN=0;

int ACTION[MAX][128],GOTO[MAX][128];

int equal(State a,State b){
    if(a.n!=b.n)return 0;
    for(int i=0;i<a.n;i++){
        int f=0;
        for(int j=0;j<b.n;j++)
            if(a.it[i].p==b.it[j].p && a.it[i].d==b.it[j].d)f=1;
        if(!f)return 0;
    }
    return 1;
}

void closure(State *s){
    int changed=1;
    while(changed){
        changed=0;
        for(int i=0;i<s->n;i++){
            Item it=s->it[i];
            if(it.d<strlen(prodR[it.p])){
                char X=prodR[it.p][it.d];
                if(X>='A'&&X<='Z'){
                    for(int j=0;j<prodN;j++){
                        if(prodL[j]==X){
                            int f=0;
                            for(int k=0;k<s->n;k++)
                                if(s->it[k].p==j && s->it[k].d==0)f=1;
                            if(!f){
                                s->it[s->n].p=j;
                                s->it[s->n].d=0;
                                s->n++;
                                changed=1;
                            }
                        }
                    }
                }
            }
        }
    }
}

State go(State s,char X){
    State ns; ns.n=0;
    for(int i=0;i<s.n;i++){
        Item it=s.it[i];
        if(it.d<strlen(prodR[it.p]) && prodR[it.p][it.d]==X){
            ns.it[ns.n].p=it.p;
            ns.it[ns.n].d=it.d+1;
            ns.n++;
        }
    }
    if(ns.n)closure(&ns);
    return ns;
}

int find(State s){
    for(int i=0;i<stN;i++) if(equal(st[i],s))return i;
    return -1;
}

void buildStates(){
    st[0].it[0].p=0;
    st[0].it[0].d=0;
    st[0].n=1;
    closure(&st[0]);
    stN=1;

    char symbols[]="aAbS";

    for(int i=0;i<stN;i++){
        for(int j=0;symbols[j];j++){
            State ns=go(st[i],symbols[j]);
            if(ns.n && find(ns)==-1)
                st[stN++]=ns;
        }
    }
}

void buildTable(){
    for(int i=0;i<MAX;i++)
        for(int j=0;j<128;j++)
            ACTION[i][j]=GOTO[i][j]=-1;

    for(int i=0;i<stN;i++){
        for(int j=0;j<st[i].n;j++){
            Item it=st[i].it[j];

            if(it.d==strlen(prodR[it.p])){
                if(it.p==0) ACTION[i]['$']=0;
                else{
                    char *t="ab$";
                    while(*t){
                        ACTION[i][*t]=-(it.p+1);
                        t++;
                    }
                }
            }
            else{
                char X=prodR[it.p][it.d];
                State ns=go(st[i],X);
                int k=find(ns);

                if(X>='A'&&X<='Z') GOTO[i][(int)X]=k;
                else ACTION[i][(int)X]=k+1;
            }
        }
    }
}

int parse(char *s){
    int stack[MAX],top=0,i=0;
    stack[0]=0;

    while(1){
        int act=ACTION[stack[top]][(int)s[i]];

        if(act==-1) return 0;
        if(act==0) return 1;

        if(act>0){
            stack[++top]=act-1;
            i++;
        }
        else{
            int p=-act-1;
            top-=strlen(prodR[p]);
            int g=GOTO[stack[top]][(int)prodL[p]];
            stack[++top]=g;
        }
    }
}

int main(){
    char input[30];

    buildStates();
    buildTable();

    printf("Enter string ending with $: ");
    scanf("%s",input);

    if(parse(input)) printf("Accepted\n");
    else printf("Rejected\n");

    return 0;
}