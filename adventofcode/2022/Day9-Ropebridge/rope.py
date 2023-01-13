def check_negative(s):
    try:
        f = float(s)
        if (f < 0):
            return True
        # Otherwise return false
        return False
    except ValueError:
        return False

def part_one(inputfile):

    # Read inputfile 
    with open(inputfile, 'r') as file:
        filestring = file.read()

    # Convert input into list of commands
    filelist = filestring.split('\n')
    commands = [x.split(' ') for x in filelist]

    print('Commands: ', commands)
    
    # Head & tails coordinates
    hc = [0, 0]
    tc = [0, 0]

    # List to store positions of tail
    tcl = []

    # Implementing commands and coordinate capture
    for command in commands:
        if command[0] == 'L':
            diffy = hc[1] - tc[1]
            for digit in range(int(command[1])):
                hc[0] -= 1
                diffx = hc[0] - tc[0]
                print('hc: ', hc, 'diffx: ', diffx)

                if diffx == -2 and diffy == -1:
                    tc[0] -= 1
                    tc[1] -= 1

                elif diffx == -2 and diffy == 1:
                    tc[0] -= 1
                    tc[1] += 1

                elif diffx == -2:
                    tc[0] -= 1
                    
                tcc = tc.copy()
                tcl.append(tcc)
                print('tcc: ', tcc, 'tcl: ', tcl)

        elif command[0] == 'R':
            diffy = hc[1] - tc[1]
            for digit in range(int(command[1])):
                hc[0] += 1
                diffx = hc[0] - tc[0]

                if diffx == 2 and diffy == 1:
                    tc[0] += 1
                    tc[1] += 1

                elif diffx == 2 and diffy == -1:
                    tc[0] += 1
                    tc[1] -= 1

                elif diffx == 2:
                    tc[0] += 1

                tcc = tc.copy()
                tcl.append(tcc)
                
        elif command[0] == 'U':
            diffx = hc[0] - tc[0]
            for digit in range(int(command[1])):
                hc[1] += 1
                diffy = hc[1] - tc[1]

                if diffx == 1 and diffy == 2:
                    tc[0] += 1
                    tc[1] += 1

                elif diffx == -1 and diffy == 2:
                    tc[0] -= 1
                    tc[1] += 1

                elif diffy == 2:
                    tc[1] += 1
                    
                tcc = tc.copy()
                tcl.append(tcc)

        elif command[0] == 'D':
            diffx = hc[0] - tc[0]
            for digit in range(int(command[1])):
                hc[1] -= 1
                diffy = hc[1] - tc[1]
                if diffx == 1 and diffy == -2:
                    tc[0] += 1
                    tc[1] -= 1

                elif diffx == -1 and diffy == -2:
                    tc[0] -= 1
                    tc[1] -= 1

                elif diffy == -2:
                    tc[1] -= 1

                tcc = tc.copy()
                tcl.append(tcc)

    print('TCL: ',tcl)

    # Count coordinates with a check list
    chk = []
    count = 0
    for coord in tcl:
        if coord in chk:
            pass
        else:
            chk.append(coord)
            count +=1
    
    print('Count: ', count)

part_one("placeholder.txt")
