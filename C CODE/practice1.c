#include <stdio.h>

// Define the structure 'country'
struct Country
{
    char name[50];
    long population;
    char language[50];
};

int main()
{
    // Declare an array of structures to store data for 3 countries
    struct Country countries[3];

    // Input data for 3 countries
    for (int i = 0; i < 3; i++)
    {
        printf("Enter details for Country %d:\n", i + 1);
        printf("Name: ");
        scanf("%s", countries[i].name);
        printf("Population: ");
        scanf("%ld", &countries[i].population);
        printf("National Language: ");
        scanf("%s", countries[i].language);
        printf("\n");
    }

    // Find the country with the lowest population
    long lowestPopulation = countries[0].population;
    int indexLowestPopulation = 0;

    for (int i = 1; i < 3; i++)
    {
        if (countries[i].population < lowestPopulation)
        {
            lowestPopulation = countries[i].population;
            indexLowestPopulation = i;
        }
    }

    // Display the country with the lowest population
    printf("Country with the lowest population:\n");
    printf("Name: %s\n", countries[indexLowestPopulation].name);
    printf("Population: %ld\n", countries[indexLowestPopulation].population);
    printf("National Language: %s\n", countries[indexLowestPopulation].language);

    return 0;
}
