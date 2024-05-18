#include <stdio.h>
int main()
{
    float temperatures[10];
    for (int i = 0; i < 10; i++)
    {
        printf("Enter temperature for City %d: ", i + 1);
        scanf("%f", &temperatures[i]);
    }
    float minTemp = temperatures[0];
    int minCityIndex = 0;
    for (int i = 1; i < 10; i++)
    {
        if (temperatures[i] < minTemp)
        {
            minTemp = temperatures[i];
            minCityIndex = i;
        }
    }
    float maxTemp = temperatures[0];
    int maxCityIndex = 0;
    for (int i = 1; i < 10; i++)
    {
        if (temperatures[i] > maxTemp)
        {
            maxTemp = temperatures[i];
            maxCityIndex = i;
        }
    }
    printf("City with Minimum Temperature:\n");
    printf("City %d: %.2f degrees Celsius\n", minCityIndex + 1, minTemp);
    printf("City with Maximum Temperature:\n");
    printf("City %d: %.2f degrees Celsius\n", maxCityIndex + 1, maxTemp);
    return 0;
}