def valid_solution(board):
    top_squares = [[],[],[]]
    mid_squares = [[],[],[]]
    low_squares = [[],[],[]]

    for line_id, line in enumerate(board):
        if 0 in line:
            return False
        line_string = repr(line).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
        if line_id <= 2:
            top_squares[0].append(line_string[0:3])
            top_squares[1].append(line_string[3:6])
            top_squares[2].append(line_string[6:])
        elif line_id <= 5:
            mid_squares[0].append(line_string[0:3])
            mid_squares[1].append(line_string[3:6])
            mid_squares[2].append(line_string[6:])
        else:
            low_squares[0].append(line_string[0:3])
            low_squares[1].append(line_string[3:6])
            low_squares[2].append(line_string[6:])

        for number_id, number in enumerate(line):
            if line.count(number) > 1:
                return False

            if line_id == 0:
                for i in range(1,8):
                    if number == board[i][number_id]:
                        return False
     
            elif line_id == 8:
                for i in range(0,7):
                    if number == board[i][number_id]:
                        return False

            else:
                for i in range(0,line_id - 1):
                    if number == board[i][number_id]:
                        return False
                
                for i in range(line_id + 1,8):
                    if number == board[i][number_id]:
                        return False

    top_squares_final = [["".join(top_squares[0])], ["".join(top_squares[1])], ["".join(top_squares[2])]]
    mid_squares_final = [["".join(mid_squares[0])], ["".join(mid_squares[1])], ["".join(mid_squares[2])]]
    low_squares_final = [["".join(low_squares[0])], ["".join(low_squares[1])], ["".join(low_squares[2])]]
    print("Top squares: ", top_squares_final)

    for square in top_squares_final:
        for number in square[0]:
            print("Square: ", square, "Number: ", number, "Occurences: ", square.count(number))
            if square[0].count(number) > 1:
                return False

    for square in mid_squares_final:
        for number in square[0]:
            if square[0].count(number) > 1:
                return False

    for square in low_squares_final:
        for number in square[0]:
            if square[0].count(number) > 1:
                return False
    
    return True