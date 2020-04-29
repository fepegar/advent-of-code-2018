#include <stdio.h>
#include <stdlib.h>

#define MATRIX_SIZE 300

int find_largest_power(int matrix[][MATRIX_SIZE], int *largest_coordinates, int size)
{
    int largest_power = 0;
    int power;
    int x, y;

    fill_matrix(matrix, 3214);

    for (int i = 0; i < MATRIX_SIZE - 2; i++)
    {
        for (int j = 0; j < MATRIX_SIZE - 2; j++)
        {
            power = 0;
            for (int di = 0; di < size; di++)
            {
                for (int dj = 0; dj < size; dj++)
                {
                    power += matrix[i + di][j + dj];
                    if (size == 4 && power > 1000)
                    {
                        printf("WAAT\n");
                        printf("Power: %d\n", power);
                        printf("Value: %d\n", matrix[i + di][j + dj]);
                        printf("i,j: %d,%d\n\n", i, j);
                    }
                }
            }
            // printf("%d ", power);
            if (power > largest_power)
            {
                x = j + 1;
                y = i + 1;
                largest_coordinates[0] = x;
                largest_coordinates[1] = y;
                largest_power = power;
            }
        }
    }
    // printf("largest_power: %d\n", largest_power);
    return largest_power;
}


void fill_matrix(int matrix[][MATRIX_SIZE], int serial_number)
{
    int rack_id;
    int power;
    int x, y;
    for (int i = 0; i < MATRIX_SIZE; i++)
    {
        for (int j = 0; j < MATRIX_SIZE; j++)
        {
            x = j + 1;
            y = i + 1;
            rack_id = x + 10;
            power = rack_id * y;
            power += serial_number;
            power *= rack_id;
            power = (power / 100) % 10;  // 12345 -> 123 -> 3
            power -= 5;
            matrix[i][j] = power;
            if (power > 1000) {
                printf("OMG");
                printf("i, j: %d,%d\n", i, j);
                printf("power: %d\n\n", power);
            }
        }
    }
}


void find_largest_size(int matrix[][MATRIX_SIZE], int *answer)
{
    int power;
    int largest_power = 0;
    int largest_power_size = 0;
    int coordinates[2];
    for (int size = 1; size <= MATRIX_SIZE; size++)
    {
        power = find_largest_power(matrix, coordinates, size);
        printf("Power: %d\n", power);
        if (power > largest_power)
        {
            largest_power = power;
            answer[0] = coordinates[0];
            answer[1] = coordinates[1];
            answer[2] = size;
            printf("X,Y,size: %d,%d,%d\n\n", answer[0], answer[1], answer[2]);
        }
    }
}


void part_1(int matrix[][MATRIX_SIZE], int *answer)
{
    int any_size = 0;
    find_largest_power(matrix, answer, 3);
}


void part_2(int matrix[][MATRIX_SIZE], int *answer)
{
    int any_size = 1;
    find_largest_size(matrix, answer);
}


int main(int argc, char *argv[])
{
    int serial_number;
    int matrix[MATRIX_SIZE][MATRIX_SIZE];
    int answer_1[2];
    int answer_2[3];

    if (argc < 2)
        serial_number = 3214;
    else
        serial_number = atoi(argv[1]);

    fill_matrix(matrix, serial_number);

    printf("Part 1:\n");
    part_1(matrix, answer_1);
    printf("Answer 1: %d,%d\n", answer_1[0], answer_1[1]);

    printf("Part 2:\n");
    part_2(matrix, answer_2);
    printf("Answer 2: %d,%d,%d\n", answer_2[0], answer_2[1], answer_2[2]);
    return 0;
}
