#!/bin/env python3

if __name__ == '__main__':
    mylist = []
    N = int(input())
    for i in range(N):
        cmd = input().strip().split()
        # print(repr(cmd))
        if cmd[0] == "insert":
            mylist.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "remove":
            mylist.remove(int(cmd[1]))
        elif cmd[0] == "append":
            mylist.append(int(cmd[1]))
        elif cmd[0] == "print":
            print(mylist)
        elif cmd[0] == "sort":
            mylist.sort()
        elif cmd[0] == "pop":
            mylist.pop()
        elif cmd[0] == "reverse":
            mylist.reverse()
