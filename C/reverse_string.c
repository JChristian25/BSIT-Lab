#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void) 
{
    char* word = "Hello, World!";
    printf("Word: %s\n", word);

    char* reversed_word = (char*)malloc(sizeof(char) * (strlen(word) + 1));
    
    for (int i = 0; i < strlen(word); i++)
    {
        reversed_word[i] = word[strlen(word) - i - 1];
    }

    reversed_word[strlen(word)] = '\0';

    printf("Reversed: %s\n", reversed_word);

    return 0;
}