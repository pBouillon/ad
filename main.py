#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os         import fork
from os         import name     as currentOS
from os         import setsid
from os         import system
from random     import randint
from subprocess import call
from sys        import exit
from time       import sleep

HOUR       = 3600
HALF       = 1800
MINUTE     = 60

if __name__ == "__main__":
    pid = fork()
    if pid==0:
        setsid()
        pid = fork()
        if pid==0:
            while True:
                sleep(randint(0,HALF))
                if currentOS == 'nt':
                    system("start %windir%\explorer.exe")
                else:
                    call(["xterm","-b","5000","vim"])
        else:
            exit(0)
    else:
        exit(0)
