#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <stdlib.h>

void first(int *question, int *score);
void second(int *question, int *score);
void third(int *question, int *score);

int main (void)
{
    int score = 0;
    int question = 1;

    system("cls");

    char name [50];
    printf("Enter your name: ");
    scanf("%s", name);

    getchar();

    printf("Welcome to Quiz Game, %s\n", name);

    while (question <= 3)
    {
        switch (question)
        {
            case 1:
                first(&question, &score);
                break;
            case 2:
                system("cls");
                second(&question, &score);
                break;
            case 3:
                system("cls");
                third(&question, &score);
                break;
        }
    }

    system("cls");
    printf("Game Over! Your final score is %d out of 3.\n", score);
    return 0;
}

void first (int *question, int *score)
{
    printf("Question 1: Who invented the telephone?\n");
    printf("A. Alexander Graham Bell\n");
    printf("B. Bill Games\n");
    printf("C. John Christian\n");

    char c;
    printf("Enter your choice (A/B/C): ");
    scanf(" %c", &c);

    if (c == 'A')
    {
        printf("Correct! Alexander Graham Bell is the inventor of the telephone.\n");
        (*score)++;
    }
    else
    {
        printf("Sorry, you got the incorrect answer.\n");
    }
    (*question)++;
    Sleep(1000);
}

void second (int *question, int *score)
{
    printf("Question 2: Who created the microscope?\n");
    printf("A. Hans and Zacharias Janssen\n");
    printf("B. John Christian\n");
    printf("C. George Winston Churchill\n");

    char c;
    printf("Enter your choice (A/B/C): ");
    scanf(" %c", &c);
    
    if (c == 'A')
    {
        printf("Correct! Hans and Zacharias Janssen created the microscope.\n");
        (*score)++;
    }
    else
    {
        printf("Sorry, you got the incorrect answer.\n");
    }
    (*question)++;
    Sleep(1000);
}

void third (int *question, int *score)
{
    printf("Question 3: What is the farthest planet in our Solar System?\n");
    printf("A. Neptune\n");
    printf("B. Pluto\n");
    printf("C. Mars\n");

    char c;
    printf("Enter your choice (A/B/C): ");
    scanf(" %c", &c);

    if (c == 'A')
    {
        printf("Correct! Neptune is the farthest planet in our Solar System!\n");
        (*score)++;
    }
    else {
        printf("Sorry, you got the incorrect answer.\n");
    }
    (*question)++;
    Sleep(1000);
}