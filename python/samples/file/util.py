#!/usr/bin/python3

import os

'''
utility function for file operation
checkfile exist
create file
'''

# check if a file or dir 'file_dir' exists
def fd_exists(file_dir, isdir=False):
    return ( os.path.exists( file_dir ) and (os.path.isdir(file_dir) or isdir))

# create a dir if it does not exist
def dirmake(path, perm = 0o755):
    if(not fd_exists(path, True)):
        os.makedirs(path, perm)

if __name__ == "__main__":
    print(fd_exists('writer.py'))
    dirmake('test')
