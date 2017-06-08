#!/bin/env python3
#
# hackerrank.com
# https://www.hackerrank.com/challenges/nested-list
#
# INPUT: first line N, number of students
#        2N subsequent lines describe ea student over 2 lines
#        - line 1: student's name
#        - line 2: grade
# Constraints:
# 2<= N <= 5
# there will always be one or more students having the second lowest grade
#
# OUTPUT: print the name(s) of any student(s) having the second lowest
# grade
# if there are multiple sutdents, order their names, alphabetically and
# print each one on a new line.
#
#


if __name__ == '__main__':
    # A list for holding the students.
    students = []
    # Loop over each student putting their name and score into a
    # list inside a list.
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find sorted uniq grades in s.
    # second lowest s[1]
    # print those students with the second lowest score
    # in sorted alpha order of their names.
    second_lowest = sorted(set([i[1] for i in students]))[1]

    for name in sorted(i[0] for i in students if i[1] == second_lowest):
        print(name)
