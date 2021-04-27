def next_bigger(n):

    stringinput = str(n)

    possibilities = []

    for i, digit in enumerate(stringinput):

        for x, seconddigit in enumerate(stringinput[i:]):

            if digit > seconddigit:

                placeholder = stringinput[:i-1] + digit + stringinput[i:x] + seconddigit + stringinput[x + 1:]
                print("x: ", x, "\ni: ", i, "\nplaceholder: ", placeholder, "\nstringinput[:i-1]: ", stringinput[:i-1], "\nseconddigit: ", seconddigit, "\nstringinput[i + 1:x]: ", stringinput[i + 1:x], "\ndigit: ", digit, "\nstringinput[x + 1:]: ", stringinput[x + 1:])
                if int(placeholder) > n:
                    possibilities.append(placeholder)

    if possibilities:

        nextNumber = min(possibilities)
        return nextNumber

    else:

        return -1

print("\nFirst Case: \n", next_bigger(12))
print("\nSecond Case: \n", next_bigger(513))
