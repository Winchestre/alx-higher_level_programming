#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in range(len(line)):
            end_line = ' ' if i != len(line) - 1 else ''
            print("{:d}".format(line[i]), end=end_line)
        print()
