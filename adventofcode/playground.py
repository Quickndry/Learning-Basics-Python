# This is just a notepad used for temporary saving of code
    for i, element in enumerate(content_string):

        if element == '.':
            placeholder.append('.')

        elif element == 'L':
            try:
                if content_string(i) & content_string(i - 1) & content_string(i + 1) == "L":
                    placeholder.append("#")
                else:
                    placeholder.append("L")
            except IndexError:
                try:
                    if content_string(i) & content_string(i + 1) == "L":
                        placeholder.append("#")
                    else:
                        placeholder.append("L")
                except IndexError:
                    if content_string(i) & content_string(i - 1) == "L":
                        placeholder.append("#")
                    else:
                        placeholder.append("L")

        elif element == '#':
            try:
                sample = ''
                sample.append(content_string(i - 1), content_string(i + 1), content_string(i + row_len), content_string(i - row_len), content_string(i + row_len - 1), content_string(i + row_len + 1), content_string(i - row_len + 1), content_string(i - row_len -1))
                occupied_seats = sample.count('#')
                if occupied_seats > 3:
                    placeholder.append('L')
                else:
                    placeholder.append('#')
            except IndexError:
                try:
                    sample = ''
                    sample.append(content_string(i + 1), content_string(i + row_len), content_string(i - row_len), content_string(i + row_len + 1), content_string(i - row_len + 1))
                    occupied_seats = sample.count('#')
                    if occupied_seats > 3:
                        placeholder.append('L')
                    else:
                        placeholder.append('#')
                except IndexError:
                    try:
                        sample = ''
                        sample.append(content_string(i - 1), content_string(i + row_len), content_string(i - row_len), content_string(i + row_len - 1), content_string(i - row_len -1))
                        occupied_seats = sample.count('#')
                        if occupied_seats > 3:
                            placeholder.append('L')
                        else:
                            placeholder.append('#')

        elif element == 'B':
