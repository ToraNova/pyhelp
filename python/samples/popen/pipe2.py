# this creates pipe that are of the OS's nature
# equivalent to doing something like this '|'

import os
import subprocess

if __name__ == '__main__':
    # creates a (python-named)pipe
    stdin_read, stdin_write = os.pipe()

    os.write(stdin_write, 15*b'\xaa\xbb\xcc\xdd')
    os.write(stdin_write, b'\xde\xad\xbe\xef')

    proc = subprocess.Popen(['xxd'], stdin = stdin_read)
