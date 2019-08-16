### VARIABLES ###
##
## Units in Pixels tuple(map(int, (to be adjusted as needed)
##

MAX_BOND_LENGTH = 10    # maximum distance before discounting a bond

RADIUS = 7           # radius of circles to be drawn for columns

##
## Colors for tracking tuple(map(int, (only up to 6 for now)
##
def red(val):
    return tuple(map(int, (val, 0, 0)))

def green(val):
    return tuple(map(int, (0, val, 0)))

def blue(val):
    return tuple(map(int, (0, 0, val)))

def yellow(val):
    return tuple(map(int, (val, val, 0)))

def magenta(val):
    return tuple(map(int, (val, 0, val)))

def cyan(val):
    return tuple(map(int, (0, val, val)))
## Other Colors
def white(val):
    return tuple(map(int, (val, val, val)))