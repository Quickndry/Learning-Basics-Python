import math

def make_readable(seconds):
    hoursFloat = seconds / 3600
    hours = math.floor(hoursFloat)
    hoursLeftover = hoursFloat % 1

    minutesFloat = hoursLeftover * 60
    minutes = math.floor(minutesFloat)
    minutesLeftover = minutesFloat % 1
    
    secondss = round(minutesLeftover * 60)
    
    if len(str(hours)) < 2:
        if hours < 10:
            hours = "0" + str(hours)
        if hours == 0:
                hours = "00"

    if len(str(minutes)) < 2:
        if minutes < 10:
            minutes = "0" + str(minutes)
        if minutes == 0:
                minutes = "00"

    if len(str(secondss)) < 2:
        if secondss < 10:
            secondss = "0" + str(secondss)
        if secondss == 0:
                secondss = "00"

    outputString = str(hours) + ":" + str(minutes) + ":" + str(secondss)
    return outputString
