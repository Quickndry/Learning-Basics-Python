def solve(a, b):
    counter = 0
    for digit in range(a, b):
        if "2" in str(digit) or "3" in str(digit) or "4" in str(digit) or "5" in str(digit) or "7" in str(digit):
            pass 
        else:
            if len(str(digit)) > 1:
                reverse_digit = str(digit)[::-1]
                converted = []
                for x in str(reverse_digit):
                    match x:
                        case "0":
                            converted.append("0")
                        case "1":
                            converted.append("1")
                        case "6":
                            converted.append("9")
                        case "8":
                            converted.append("8")
                        case "9":
                            converted.append("6")
                converted_digit = "".join(converted)
                if int(converted_digit) == digit:
                    print(converted_digit)
                    counter += 1

            else:
                match str(digit):
                    case "0":
                        counter += 1
                    case "1":
                        counter += 1
                    case "8":
                        counter += 1

    return(counter)