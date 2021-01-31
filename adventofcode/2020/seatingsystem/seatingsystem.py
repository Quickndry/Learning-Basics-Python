
# Basic working idea
# Step 1: Turn all empty seats into occupied seats.
# Step 2: Itirate through each row, using the seating rules to determine if
# people would move.
# Step 3: Repeat the process on results of Step 2.
# Step 4: Compare results of Step 3 with the results of Step 2.If the same:
# return number of occupied seats in result. If not the same, repeat Step 3
# with the result of Step 3 and compare both Step 3's first result with it's
# second result etc.

# Convert content to textvariable in which every '\n' is replaced by 'B'
# Find length of row (i.e. start to 'B')
# Use this to iterate through textvariable, replacing everything according to
# the rules.


def findseat_partone(textfile):
    placeholder_one = []
    placeholder_two = []
    placeholder_three = []

    with open(textfile, encoding='utf-8') as file:
    	content = file.read()
    	seating_rows = contents.split('\n')

# Step 1: Convert seats using rules

        for row in seating_rows:
            newrow = []
            for i, seat in enumerate(row):

                if seat == "L":
                    try:
                        if row(i) & row(i - 1) & row(i + 1) == "L":
                            newrow.append("#")
                        else:
                            newrow.append("L")
                    except IndexError:
                        try:
                            if row(i) & row(i + 1) == "L":
                                newrow.append("#")
                            else:
                                newrow.append("L")
                        except IndexError:
                            if row(i) & row(i - 1) == "L":
                                newrow.append("#")
                            else:
                                newrow.append("L")

                if seat == "#":
                    try:
                        if row(i - 4) & row(i - 3) & row(i - 2) & row(i - 1) == "#":
                            newrow.append("L")
                        else:
                            newrow.append("#")

# Step 1: Turn all empty seats into occupied seats.
        for row in seating_rows:
            newrow = []
            for seat in row:
                if seat == "L":
                    newrow.append("#")
                else:
                    newrow.append(".")
            placeholder_one.append(newrow)

# Step 2.1: Itirate through each row, using the second seating rule.

for row in placeholder:
    newrow = []

    for i in enumerate(len(row)):
        try:
            if row(i) == "L":
                if row(i - 4) & row(i - 3) & row(i - 2) & row(i - 1) == "#":
                    newrow.append("L")
                elif row(i + 4) & row(i + 3) & row(i + 2) & row(i + 1) == "#":
                    newrow.append("L")
                elif row(i) == ".":
                    newrow.append(".")
                else:
                    newrow.append("#")

        except IndexError:
            try:
                if row(i) & row(i + 1) == "L":
                    newrow.append("#")
                elif row(i) == ".":
                    newrow.append(".")
                else:
                    newrow.append("L")

            except IndexError:
                if row(i) & row(i - 1) == "L":
                    newrow.append("#")
                elif row(i) == ".":
                    newrow.append(".")
                else:
                    newrow.append("L")
    placeholder_two.append(newrow)

# Step 2.2: Itirate through each row, using the first seating rule.

        for row in placeholder:
            newrow = []

            for i in enumerate(len(row)):
                try:
                    if row(i) & row(i - 1) & row(i + 1) == "L":
                        newrow.append("#")
                    elif row(i) == ".":
                        newrow.append(".")
                    else:
                        newrow.append("L")

                except IndexError:
                    try:
                        if row(i) & row(i + 1) == "L":
                            newrow.append("#")
                        elif row(i) == ".":
                            newrow.append(".")
                        else:
                            newrow.append("L")

                    except IndexError:
                        if row(i) & row(i - 1) == "L":
                            newrow.append("#")
                        elif row(i) == ".":
                            newrow.append(".")
                        else:
                            newrow.append("L")
            placeholder_two.append(newrow)

# Step 3: Repeat the process on results of Step 2.

# L.LL.LL.LL
# #.##.##.##
# #.LL.L#.##
