import sys
import os

print('The command line arguments are:')
for i in sys.argv:
    print(i)
    
print('The PYTHPATH is', sys.path,'\n')

print(os.getcwd())
