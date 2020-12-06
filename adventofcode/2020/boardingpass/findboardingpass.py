
def findboardingpass():
    list_of_seats = []
    list_of_seatids = []
    list_of_verticalseats = []
    list_of_horizontalseats = []

    with open('boardingpass.txt') as f:
        ticket_list = f.readlines()
        ticket_list = [x.strip() for x in ticket_list]


    for ticket in ticket_list:
        vseats = [vertical for vertical in range(1, 128)]
        hseats = [horizontal for horizontal in range(0, 8)]
        print(hseats)

        for letter in ticket:

            verticalhal = len(vseats) // 2
            horizontalhal = len(hseats) // 2

            if letter == 'F': #lower halve
                placeholder = vseats[:verticalhal]
                vseats = placeholder

            elif letter == 'B': #upper halve
                placeholder = vseats[verticalhal:]
                vseats = placeholder


            elif letter == 'L': #lower halve
                placeholder = hseats[:horizontalhal]
                hseats = placeholder

            else: #upper halve
                placeholder = hseats[horizontalhal:]
                hseats = placeholder

        seatid = int(vseats[0]) * 8 + int(hseats[0])
        ticketseat = 'Row: ' + str(vseats[0]) + ', Column: ' + str(hseats[0]) + ', Seat ID: ' + str(seatid)
        list_of_seatids.append(seatid)
        list_of_horizontalseats.append(hseats[0])
        list_of_verticalseats.append(vseats[0])
        list_of_seats.append(ticketseat)

#    for test purposes:
#    print(sorted(list_of_seatids))
#    print(sorted(list_of_verticalseats))
#    print(sorted(list_of_horizontalseats))

    with open('ticketseats.txt', 'w') as ft:
        for seat in sorted(list_of_seats):
            ft.write(seat + '\n')

findboardingpass()
