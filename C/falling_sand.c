#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
#include <time.h>
#include <unistd.h>
#include <stdbool.h>

#define ROWS 10
#define COLUMNS 40

void checkState();
void setSand(int (*grid)[COLUMNS]);
void render(int rows, int columns, int (*grid)[COLUMNS]);
void loop(int rows, int columns, int (*grid)[COLUMNS]);

int main (void)
{   
    srand(time(NULL)); // Ensures that for each program execution, generates different random numbers.
    int grid[ROWS][COLUMNS] = {0};

    loop(ROWS, COLUMNS, grid);
    
    return 0;
}

void checkState(int (*grid)[COLUMNS])
{
    for (int row = ROWS; row >= 0; row--)
    {
        for (int column = 0; column < COLUMNS; column++)
        {
            if (grid[row][column] == 1)
            {
                int checkBottom = (row + 1 < ROWS) ? grid[row + 1][column] : -1; // Check below
                int checkRight = (row + 1 < ROWS && column + 1 < COLUMNS) ? grid[row + 1][column + 1] : -1; // Check bottom right
                int checkLeft = (row + 1 < ROWS && column - 1 >= 0) ? grid[row + 1][column - 1] : -1; // Check bottom left


                if (checkLeft == 0 || checkRight == 0)
                {
                    if (row <= ROWS - 1)
                    {
                        checkLeft, checkRight = -1;
                    }
                }

                if (checkBottom == 0)
                {
                    grid[row][column] = 0;
                    grid[row + 1][column] = 1;
                } else if (checkBottom != 0)
                {
                    if (checkLeft == 0)
                    {
                        grid[row][column] = 0; // Remove from current position
                        grid[row + 1][column - 1] = 1; // Move left
                    }
                    else if (checkRight == 0)
                    {
                        grid[row][column] = 0; // Remove from current position
                        grid[row + 1][column + 1] = 1; // Move right
                    }
                }
            }
        }
    }
}

void setSand(int (*grid)[COLUMNS])
{
    int rr = rand() % (ROWS + 1 - 0) + 0;
    int rc = rand() % (COLUMNS + 1 - 0) + 0;

    if (grid[rr][rc] != 1)
    {
        grid[rr][rc] = 1;
    }
}

void render(int rows, int columns, int (*grid)[COLUMNS])
{
    system("cls");
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 40; j++) {
            if (grid[i][j] == 0) {
                printf("/");
            } else {
                printf("#");
            }
        }
        printf("\n");
    }
}

void loop(int rows, int columns, int (*grid)[COLUMNS])
{
    setSand(grid);
    checkState(grid);
    render(rows, columns, grid);
    usleep(400000);
    loop(ROWS, COLUMNS, grid);
}