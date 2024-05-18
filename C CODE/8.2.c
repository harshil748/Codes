#include <stdio.h>
#include <string.h>
#define MAX_NAME_LENGTH 50
#define NUM_STUDENTS 5
int main()
{
    char names[NUM_STUDENTS][MAX_NAME_LENGTH];
    char temp[MAX_NAME_LENGTH];
    int i,j;
    printf("Enter the names of %d students:\n",NUM_STUDENTS);
    for(i=0;i<NUM_STUDENTS;i++)
    {
        printf("Student %d: ",i+1);
        fgets(names[i],MAX_NAME_LENGTH,stdin);
        names[i][strcspn(names[i],"\n")]='\0';
    }
    for(i=0;i<NUM_STUDENTS-1;i++)
    {
        for(j=i+1;j<NUM_STUDENTS;j++)
        {
            if(strcmp(names[i],names[j])>0)
            {
                strcpy(temp, names[i]);
                strcpy(names[i], names[j]);
                strcpy(names[j], temp);
            }
        }
    }
    printf("\nSorted names:\n");
    for(i=0;i<NUM_STUDENTS;i++)
    {
        printf("%s\n", names[i]);
    }
    return 0;
}