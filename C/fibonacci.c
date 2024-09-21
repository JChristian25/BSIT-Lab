#include <stdio.h>

int fibonacci(int num_a, int num_b, int turns);

int main(void)
{
    int num_a = 1;
    int num_b = 2;
    int turns = 5;
    int sum = fibonacci(num_a, num_b, turns);

    printf("Number: %d, %d\nTurns: %d\nSum: %d\n", num_a, num_b, turns, sum);
    return 0; 
}

int fibonacci(int num_a, int num_b, int turns)
{
    printf("Number: %d, %d\nTurns: %d\n", num_a, num_b, turns);
    
    if (turns == 0) 
    {
        return num_a; 
    }
    
    int sum = num_a + num_b;
    return fibonacci(num_b, sum, turns - 1); 
}
