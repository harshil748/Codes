#include <stdio.h>

int tempCount = 1;
int labelCount = 1;

void newLabel(char *label)
{
    sprintf(label, "L%d", labelCount++);
}

int main()
{

    char L1[10], L2[10], L3[10], L4[10], L5[10], L6[10];

    newLabel(L1);
    newLabel(L2);
    newLabel(L3);
    newLabel(L4);
    newLabel(L5);
    newLabel(L6);

    printf("if cgpa >= 8.5 goto %s\n", L1);
    printf("goto %s\n", L4);

    printf("%s:\n", L1);
    printf("if income < 400000 goto %s\n", L2);
    printf("goto %s\n", L3);

    printf("%s:\n", L2);
    printf("call approveScholarship\n");
    printf("goto %s\n", L6);

    printf("%s:\n", L3);
    printf("call forwardForReview\n");
    printf("goto %s\n", L6);

    printf("%s:\n", L4);
    printf("if cgpa >= 7.0 goto %s\n", L5);
    printf("goto reject\n");

    printf("%s:\n", L5);
    printf("if sportsQuota == 1 goto sports\n");
    printf("goto reject\n");

    printf("sports:\n");
    printf("call approveSportsScholarship\n");
    printf("goto %s\n", L6);

    printf("reject:\n");
    printf("call rejectApplication\n");

    printf("%s:\n", L6);
    printf("end\n");

    return 0;
}