#!/usr/bin/python3

# print stdout of process even before process terminates
# this is much more like terminal behaviour instead
# of out,err = proc.communicate(), which BLOCKS until
# proc has terminated.

import subprocess

# example command, each element is an argument
cmd = ["ping","8.8.8.8"]
# run the command
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
for line in iter(proc.stdout.readline, ""):
    print(line, end="")
# process has no more lines (therefore the above for-loop exits)
proc.stdout.close()
# obtain return code (0 for OK)
rc = proc.wait()
