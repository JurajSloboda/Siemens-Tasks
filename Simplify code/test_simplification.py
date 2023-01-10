#!/usr/bin/env python3
import original_code
import simplified

"""tests if simplified code returns same values as original"""
def test_1():
    test = [1,1,1,2,1,5,4]
    assert original_code.fool(test) == simplified.simplified(test)

def test_2():
    test = ["asd","das","asd","qwe"]
    assert original_code.fool(test) == simplified.simplified(test)

def test_3():
    test = [1,1,"asd","das","asd","qwe",1,5,4]
    assert original_code.fool(test) == simplified.simplified(test)