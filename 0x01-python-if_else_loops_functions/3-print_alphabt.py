#!/usr/bin/python3
print(''.join([chr(letter) for letter in range(ord('a'),
        ord('z')+1) if chr(letter) not in ['q', 'e']]), end='')
