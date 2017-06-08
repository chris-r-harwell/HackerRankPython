#!/bin/env python3
"""
https://www.hackerrank.com/challenges/decorators-2-name-directory
    Let's use decorators to buid a name directory! You are given some
    information about N people. Each person has a first name, last name,
    age and sex. Print their names in a specific format sorted by their
    age in ascending order i.e. the youngest person's name should be
    printed first. For two people of the same age, print them in the
    order of their input.

For Henry Davids, the output should be:

    Mr. Henry Davids

For Mary George, the output should be:

    Ms. Mary George

INPUT:
     1st line: integer, N, number of people N lines, each containing the
     space separated values of the first name, last name, age and sex,
     respectively.

Constraints:
    1<= N <= 10

Output Format:
    Output N names on separate lines in the format described above in
    ascending order of age.

Concept:
    For sorting a nested list based on some parameter, you can use the
    itemgetter library.


"""
import operator


def person_lister(f):
    def inner(people):
        # complete the function
        # return f(people)
        mylist = []
        for person in people:
            mylist.append(name_format(person))
        people = mylist

    return inner


@person_lister
def name_format(person):
    title = ("Mr." if person[3] == "M" else "Ms.")
    return " ".join([title, person[0], person[1]])


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    # Sort the people in the list of lists by age using operator itemgetter.
    people.sort(key=operator.itemgetter(2))
    print(*name_format(people), sep='\n')
