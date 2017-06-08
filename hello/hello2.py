#!/usr/bin/env python2

import argparse
import sys
import string

def main(args):
    print 'Hello there', " ".join(args.rstring)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A hello there program which may have a string on the right.')
    parser.add_argument(
        'rstring', nargs = '*',
        help='add another word or phrase to the right of hello there')
    args = parser.parse_args()
    main(args)
