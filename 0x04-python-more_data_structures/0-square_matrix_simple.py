#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	square = []
	for i in matrix:
		square.append([j*j for j in i])
	return square
