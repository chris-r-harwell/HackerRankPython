#!/bin/env python3
#
"""

 https://www.hackerrank.com/challenges/the-minion-game

 Rules:
 Both players are given the same string, S.
 Bother players have to make substrings using letters of the string S.
 Sutart has to make words starting with consonants.
 Kevin has to make words starting with vowels, here
 only defined as AEIOU (in this problem Y is not a vowel).
 The game ends when both players have made all possible substrings.

 Scoring:
 A players gets +1 point for each occurence of the substring in the string S.

 Example:
 S =BANANA
 Kevin's vowel beginning word = ANA
 Here, ANA occurs twice in BANANA. Hence Kevin will get 2 points.

 Task:
 Determine the winner of the game and their score.

 Input:
 a ginel line of input containing the string S.
 Note: The string S will contain only uppercase letters: [A-Z]
 Contraints:
 0 < len(S) <= 10^6

 Output:
 Print one line:
 the name of the winner and their score separeted by a space.
 If the game is a draw print Draw
"""


def minion_game(string):
    """
    Start the minion game with kevin and stuart both having a 0 score.
    Slice the string with a start and an end over all the substrings.
    Check the first letter and if it is a vowel add a point for kevin,
    otherwise it is a consonant and add a point for stuart.
    """
    vowels = ('A', 'E', 'I', 'O', 'U')
    kevin = 0
    stuart = 0
    length = len(string)
    for start in range(0, length):
        for end in range(start + 1, length + 1):
            substring = s[start:end]
            if substring[0] in vowels:
                kevin += 1
            else:
                stuart += 1

    # Find and print the winner and score or Draw
    if stuart > kevin:
        print('Stuart {}'.format(stuart))
    elif kevin > stuart:
        print('Kevin {}'.format(kevin))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
