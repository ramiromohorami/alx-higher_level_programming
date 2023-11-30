#!/usr/bin/pytho3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

def uppercase(word):
    for c in word:
        if not islower(c):
            print("{:c}".format(ord(c)), end="")
        else:
            print("{:c}".format(ord(c) - 32), end="")
    print("")
