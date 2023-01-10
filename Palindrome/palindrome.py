#!/usr/bin/env python3

import sys

if sys.argv[1] == sys.argv[1][::-1]:
    print("word " + sys.argv[1] + " is a palindrome")
else:
    print("word " + sys.argv[1] + " is not a palindrome")

