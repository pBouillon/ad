#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os         import fork
from os         import setsid
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
                call(["xterm","-b","5000","vim"])
        else:
            exit(0)
    else:
        exit(0)
