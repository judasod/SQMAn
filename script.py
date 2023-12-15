#!/usr/bin/python3
import sys
import os


print('[*]', "AXFR Zone Transfer")
print('[*]', "Usage: ", sys.argv[0], ' + ', "DOMAIN")

if len(sys.argv) == 1:
    # Checks if domain name is supplied as parameter
    print('No arguments!')
else:
    cm = 'for sv in $(host -t ANY ' +sys.argv[1] + ' | cut -d " " -f4); do \nhost -l ' +sys.argv[1] + ' $sv | grep "has addr"\ndone'
    print('[*]', "Searching records for domain: ", sys.argv[1], "\n")
    # Command is limited to Linux environments  only
    os.system(cm)
    os.system('echo $?')

