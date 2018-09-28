# coding: utf-8
#!/usr/bin/env python
from random import *
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
def banner():
    header = color.RED + """

SERIA CYBER TOOL



"""


    oblique = color.PURPLE + """

SERIA CYBER TOOL

"""

    modular = color.YELLOW + """

SERIA CYBER TOOL
"""

    speed = color.GREEN + """

SERIA CYBER TOOL

"""



    skull = color.CYAN + """


SERIA CYBER TOOL
"""
    lastthing = color.OKBLUE + """


SERIA CYBER TOOL
"""
    lol = color.WARNING + """

SERIA CYBER TOOL

"""
    headers = [header, oblique, modular, speed, skull, lastthing, lol]
    print headers[randint(0,6)]
