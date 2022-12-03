# x = loose = 0
# z = draw = 3
# y = win = 6
# a = Rock = 1
# b = Paper = 2
# c = Scissor = 3
# win = 6
# draw = 3
# loss = 0


def rps_score(txtfile):
    file = open(txtfile, 'r')
    lines = file.readlines()
    score = 0
    for line in lines:
        line_adapted = line.replace("\n", "")
        line_components = line_adapted.split(' ')
        if line_components[0] == 'A':
            if line_components[1] == 'X':
                score += 3
            elif line_components[1] == 'Y':
                score += 4
            else:
                score += 8
            
        elif line_components[0] == 'B':
            if line_components[1] == 'X':
                score += 1
            elif line_components[1] == 'Y':
                score += 5
            else:
                score += 9

        else:
            if line_components[1] == 'X':
                score += 2
            elif line_components[1] == 'Y':
                score += 6
            else:
                score += 7

    return score

print(rps_score('input.txt'))