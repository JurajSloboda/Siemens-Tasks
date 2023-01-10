#!/usr/bin/env python3\

def simplified(items):
    #load list items into dicitonary so delete duplicates but keep order and make list back again
    return list(dict.fromkeys(items))

