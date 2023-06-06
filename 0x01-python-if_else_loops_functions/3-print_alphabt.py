#!/usr/bin/python3
for char_code in range(ord('a'), ord('z')+1):
    if chr(char_code) not in 'qe':
        print("{}".format(chr(char_code)), end='')
