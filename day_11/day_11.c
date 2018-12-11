#include <stdio.h>
#include <stdlib.h>

#define MATRIX_SIZE 300

void *find_largest_power(int serial_number, int *largest_coordinates)
{
    int matrix[MATRIX_SIZE][MATRIX_SIZE];
    int largest_power = 0;
    int rack_id;
    int power;
    int aux;
    int debug = 0;
    int xd = 33;
    int yd = 45;
    for (int y = 1; y <= MATRIX_SIZE; y++)
    {
        for (int x = 1; x <= MATRIX_SIZE; x++)
        {
            rack_id = x + 10;
            if (x == xd && y == yd && debug) printf("Rack ID: %d\n", rack_id);
            power = rack_id * y;
            if (x == xd && y == yd && debug) printf("Power: %d\n", power);
            power += serial_number;
            if (x == xd && y == yd && debug) printf("Power: %d\n", power);
            power *= rack_id;
            if (x == xd && y == yd && debug) printf("Power: %d\n", power);
            power = (power / 100) % 10;  // 12345 -> 123 -> 3
            if (x == xd && y == yd && debug) printf("Power: %d\n", power);
            power -= 5;
            if (x == xd && y == yd && debug) printf("Power: %d\n", power);
            if (power > largest_power)
            {
                printf("Largest: %d\n", largest_power);
                largest_power = power;
                largest_coordinates[0] = x;
                largest_coordinates[1] = y;
            }
            // printf("Power: %d\n", power);
        }
    }
}


void *part_1(int serial_number, int *answer)
{
    find_largest_power(serial_number, answer);
}


int part_2(int serial_number)
{
    int answer = -1;
    return answer;
}


int main(int argc, char *argv[])
{
    int data;
    if (argc < 2)
        data = 3214;
    else
        data = atoi(argv[1]);
    printf("Part 1:\n");
    int answer_1[2];
    part_1(data, answer_1);
    printf("Answer 1: %d,%d\n", answer_1[0], answer_1[1]);
}
