def customsdecl():
    yes_by_all = 0

    #Open Txt file and convert content to list
    with open('input.txt', encoding='utf-8') as file:
	       contents = file.read()
	       list_of_groups = contents.split('\n\n')
    print(list_of_groups)

    #Loop through groups inside list
    for group in list_of_groups:
        number_of_respondents = 1

        #Loop through every answer given in a group
        for answer in group:

            print("Input Answers: ")
            print(answer)

            #Find number of people who answered questions
            if answer == '\n':
                number_of_respondents += 1
            else:
                pass

        print("Number of Respondents: ")
        print(number_of_respondents)
        print("\n")

        for i in group:

            print("Count of letter prevalence: ")
            print(group.count(i))


            if group.count(i) == number_of_respondents:
                yes_by_all += 1
                print("Valid Answer: ")
                print(yes_by_all)
                print("\n")
            else:
                print("Valid Answer: ")
                print(yes_by_all)
                print("\n")
                pass
        print("\n\n")

    print(yes_by_all)

    return yes_by_all


customsdecl()
