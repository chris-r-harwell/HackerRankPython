#!/bin/env python3
#
# https://www.hackerrank.com/challenges/finding-the-percentage
#
# INPUT: first line N, number of students
#        2N subsequent lines describe ea student over 2 lines
#        - line 1: student's name
#        - line 2: grade
# Constraints:
# 2<= N <= 10
# 0 <= Marks <= 100
#
# OUTPUT: Print one line: average marks by student 2 decimal places.
#

if __name__ == '__main__':
    n = int(input())
    # A dictionary for holding the student, score lists.
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    average = sum(marks)/len(marks)
    print("{:.2f}".format(average))
