#include <stdio.h>
int main()
{
    FILE *file;
    char letter;
    long fileSize;
    file = fopen("ALPHABETS.txt", "w");
    if (file == NULL)
    {
        perror("Error creating the file");
        return 1;
    }
    for (letter = 'A'; letter <= 'Z'; letter++)
    {
        fputc(letter, file);
    }
    fclose(file);
    file = fopen("ALPHABETS.txt", "r");
    if (file == NULL)
    {
        perror("Error opening the file for reading");
        return 1;
    }
    fseek(file, 0, SEEK_END);
    fileSize = ftell(file);
    for (long i = fileSize - 1; i >= 0; i--)
    {
        fseek(file, i, SEEK_SET);
        putchar(fgetc(file));
    }
    putchar('\n');
    fclose(file);
    return 0;
}