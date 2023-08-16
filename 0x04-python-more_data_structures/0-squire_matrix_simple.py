#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Calculate square of ints in the matrix"""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
