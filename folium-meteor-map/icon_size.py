from math import log10, ceil, isnan

def iconSize(mass):
    if isnan(mass):
        result = 20
    else:
        result = 20*ceil(log10(mass))
    return result
