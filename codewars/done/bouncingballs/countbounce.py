def bouncing_ball(h, bounce, window):
    print(h, ',', bounce, ',', window)
    counter = -1

    if window > h:
        return -1
    elif bounce >= 1:
        return -1
    elif bounce <= 0:
        return -1
    elif h == 0:
        return -1
    else:
        while h > window:
            counter += 2
            h = h * bounce

    print(counter)
    return counter