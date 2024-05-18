#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    FILE *file1, *file2, *file3;
    int num;
    if (argc != 4)
    {
        printf("Usage: %s Data1.txt Data2.txt Data3.txt\n", argv[0]);
        return 1;
    }
    file1 = fopen(argv[1], "r");
    if (file1 == NULL)
    {
        perror("Error opening file1");
        return 1;
    }
    file2 = fopen(argv[2], "r");
    if (file2 == NULL)
    {
        perror("Error opening file2");
        fclose(file1);
        return 1;
    }
    file3 = fopen(argv[3], "w");
    if (file3 == NULL)
    {
        perror("Error creating file3");
        fclose(file1);
        fclose(file2);
        return 1;
    }
    while (fscanf(file1, "%d", &num) == 1)
    {
        fprintf(file3, "%d\n", num);
    }
    while (fscanf(file2, "%d", &num) == 1)
    {
        fprintf(file3, "%d\n", num);
    }
    fclose(file1);
    fclose(file2);
    fclose(file3);
    printf("Files %s and %s merged into %s.\n", argv[1], argv[2], argv[3]);
    return 0;
}