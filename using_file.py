#!/usr/bin/python
# Filename: using_file.py
poem = "Programming is fun"

f = open('poem.txt', 'w') # open for 'w'riting 
f.write(poem) # write text to file
f.close() # close the file
f = open('poem.txt') # if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print(line, end='')
f.close() # close the file