
    int rr = rand() % (ROWS + 1 - 0) + 0;
    int rc = rand() % (COLUMNS + 1 - 0) + 0;

    if (grid[rr][rc] != 1)
    {
        grid[rr][rc] = 1;
    }
}