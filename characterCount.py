#!/bin/env python3
#
# From _Automate the Boring Stuff with Python_, setdefault() Method,, p110.
#

message = 'It was a bright cold day in April , and the clocks were striking thirteenn.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
