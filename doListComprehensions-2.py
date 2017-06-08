#!/bin/env python3
#
# hackerrank.com
# https://www.hackerrank.com/challenges/list-comprehensions
#
# INPUT: four lines each with an integer
#        specifying dimensions of cube X,Y,Z and
#        constraint N
# OUTPUT: list of all possible coordinates (i,j,k) on 3D grid
# where the sum of i+j+k != N
# 0 <= i <= X
# 0 <= j <= Y
# 0 <= k <= Z
#
# Using list comprehensions
# ( to build lists without having to use different for loops to append)
# eliminates need for lambda function
# more readable than using map()
# more compact than using for loop
#
# List comprehensions can be nested where they take the following form:
#
# [ expression-involving-loop-variables for outer-loop-variable
#     in outer-sequence for inner-loop-variable in inner-sequence ]
# This is equivalent to writing:
#
# results = []
# for outer_loop_variable in outer_sequence:
#     for inner_loop_variable in inner_sequence:
#         results.append( expression_involving_loop_variables )
#
# add a filter:
#
# [ expression-involving-loop-variable for loop-variable in sequence
#     if boolean-expression-involving-loop-variable ]
#
# This form is similar to the simple form of list comprehension,
# but it evaluates boolean-expression-involving-loop-variable for every item.
# It also only keeps those members for which the boolean expression is True.
#
#  multi-variate list comprehensions
# A list comprehension consists of brackets containing an expression
# followed by a for clause, then zero or more for or if clauses. The
# result will be a new list resulting from evaluating the expression
# in the context of the for and if clauses which follow it. For example,
# this listcomp combines the elements of two lists if they are not equal:
# >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#
# nested:
# The initial expression in a list comprehension can be any arbitrary
# expression, including another list comprehension.
# >>> [[row[i] for row in matrix] for i in range(4)]



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ans_list = [[i, j, k]
                for i in range(x + 1)
                for j in range(y + 1)
                for k in range(z + 1)
                if (i + j + k) != n]

    # Print the list in lexicographic increasing order.
    ans_list.sort()
    print(repr(ans_list))
