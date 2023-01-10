#!/usr/bin/env python3
import sys

def encrypt(txt, shift):
    result = ""

    # encryption based on https://en.wikipedia.org/wiki/Caesar_cipher
    for i in range(len(txt)):
        ch = txt[i]
        
        if txt[i]==" ":
            result+=" "
        elif (txt[i].isupper()):
            result += chr((ord(txt[i]) + int(shift)-65) % 26 + 65)
        else:
            result += chr((ord(txt[i]) + int(shift)-97) % 26 + 97)
    
    return result


if __name__ == "__main__":
    
    # encrypt till keyboard interrupt
    try:
        while True:
            txt = input("Enter text to encrypt: ")
            print("Encrypted text: " + encrypt(txt, sys.argv[1]))
    except KeyboardInterrupt:
        print("\nEnd of encrypting")