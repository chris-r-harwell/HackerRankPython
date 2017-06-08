#!/bin/env python3


def doListOp( a_list, operation ):
        if operation[0] == "insert":
            a_list.insert(int(operation[1]), int(operation[2]))
        elif operation[0] == "remove":
            a_list.remove(int(operation[1]))
        elif operation[0] == "append":
            a_list.append(int(operation[1]))
        elif operation[0] == "print":
            print(a_list)
        elif operation[0] == "sort":
            a_list.sort()
        elif operation[0] == "pop":
            a_list.pop()
        elif operation[0] == "reverse":
            a_list.reverse()
        return a_list


if __name__ == '__main__':
    mylist = []
    N = int(input())
    for i in range(N):
        cmd = input().strip().split()
        mylist = doListOp(mylist, cmd)
