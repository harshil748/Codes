#include <stdio.h>
int main()
{
    FILE *sourceFile, *destinationFile;
    char ch;
    sourceFile = fopen("source.txt", "rb");
    if (sourceFile == NULL)
    {
        perror("Error opening source file");
        return 1;
    }
    destinationFile = fopen("destination.txt", "wb");
    if (destinationFile == NULL)
    {
        perror("Error opening destination file");
        fclose(sourceFile);
        return 1;
    }
    while ((ch = fgetc(sourceFile)) != EOF)
    {
        fputc(ch, destinationFile);
        putchar(ch);
    }
    if (feof(sourceFile))
    {
        printf("\nEnd of source file reached.\n");
    }
    else if (ferror(sourceFile))
    {
        perror("\nError reading source file");
    }
    fclose(sourceFile);
    fclose(destinationFile);
    return 0;
}