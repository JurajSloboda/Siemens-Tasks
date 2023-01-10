#!/usr/bin/env python3
import cipher

"""Tests of encrypt function """
def test_encrypt_1():
    assert cipher.encrypt("abcd",1) == "bcde"
    
def test_encrypt_2():
    assert cipher.encrypt("xyza",1) == "yzab"

def test_encrypt_3():
    assert cipher.encrypt("Longer text with UPPERCASE and loweracase text encryption", 10) == "Vyxqob dohd gsdr EZZOBMKCO kxn vygobkmkco dohd oxmbizdsyx"

