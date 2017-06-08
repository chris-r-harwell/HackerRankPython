#!/bin/env python3
#
# From _Automate the Boring Stuff with Python_, setdefault() Method,, p110.
#


import pprint
message = 'It was a bright cold day in April , and the clocks were striking thirteenn.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
pprint.pprint(count['n'])
print(pprint.pformat(count['n']))
