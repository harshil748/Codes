#include <stdio.h>
int main()
{
    int matchSticks = 21;
    int userPick, computerPick;
    while (1)
    {
        printf("Pick 1, 2, 3, or 4 match-sticks: ");
        scanf("%d", &userPick);
        if (userPick < 1 || userPick > 4)
        {
            printf("Invalid input. Please pick 1, 2, 3, or 4 match-sticks.\n");
            continue;
        }
        matchSticks -= userPick;
        if (matchSticks <= 0)
        {
            printf("You picked the last match-stick. You lose!\n");
            break;
        }
        computerPick = 5 - userPick;
        printf("Computer picks %d match-sticks.\n", computerPick);
        matchSticks -= computerPick;
        if (matchSticks <= 0)
        {
            printf("Computer picked the last match-stick. You win!\n");
            break;
        }
    }
    return 0;
}