import math

def calculate_fuel():
    fuelneeded = []
    with open('mass.txt', encoding='utf-8') as file:
        contents = file.read()
        list_of_groups = contents.split('\n')

    for content in list_of_groups:
        fuelone = math.floor(int(content) // 3) - 2
        print("Fuelone: ", fuelone, "\n")
        fuelneeded.append(fuelone)

        while math.floor(fuelone // 3) > 0:
            fuelone = math.floor(fuelone // 3) - 2
            print("Fuelone: ", fuelone, "\n")
            if fuelone < 0:
                fuelneeded.append(0)
            else:
                fuelneeded.append(fuelone)
        else:
            pass

    print(fuelneeded)
    print(sum(fuelneeded))

calculate_fuel()
