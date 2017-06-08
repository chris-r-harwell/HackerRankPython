#!/bin/env python3

def checkWeird(n):
    # Given an integer, n, perform the following conditional actions:
    
    # If n is odd, print Weird.
    # odd means 1 left over when divided by 2.
    if (n % 2 == 1):
        ans = "Weird"
        return ans
    
    # If n is even and in the inclusive range of  2 to 5, print Not Weird
    if( 2 <= n <= 5):
        ans = "Not Weird"
        return ans
    
    if( 6 <= n <= 20): 
        # If n is even and in the inclusive range of  6 to 20, print Weird
        ans = "Weird"
        return ans
    
    if( n > 20):
        # If n is even and greater than 20, print Not Weird
        ans = "Not Weird"
        return ans

        
if __name__ == '__main__':
    n = int(input())
    s = checkWeird(n)
    print(str(s))
