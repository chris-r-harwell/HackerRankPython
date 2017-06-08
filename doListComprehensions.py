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


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x_list = []
    y_list = []
    z_list = []
    ans_list = []

    x_list = [i for i in range(x + 1)]
    y_list = [i for i in range(y + 1)]
    z_list = [i for i in range(z + 1)]

    for i in x_list:
        for j in y_list:
            for k in z_list:
                if (i + j + k) != n:
                    ans_list.append([i, j, k])

    # Print the list in lexicographic increasing order.
    ans_list.sort()
    print(repr(ans_list))
