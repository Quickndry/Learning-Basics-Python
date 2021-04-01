import math

def spinning_wheel(wheel):
    total = len(wheel)
    wins = wheel.count('W')

    percentagew = math.floor(wins / total)
    
    return percentagew