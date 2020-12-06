
def customsdecl():
    yes_by_all = 0

    #Open Txt file and convert content to list
    with open('input.txt', encoding='utf-8') as file:
	       contents = file.read()
	       list_of_groups = contents.split('\n\n')
#    print(list_of_groups)

    #Loop through groups inside list
    for group in list_of_groups:
        number_of_respondents = 1
        already_checked = []

        #Loop through every answer given in a group
        for responses in group:

            #Find number of people who answered questions
            if responses == '\n':
                number_of_respondents += 1
            else:
                pass

        print("Number of Respondents: ")
        print(number_of_respondents)
        print("\n")

        #If only one respondent, all their answers are valid
        if number_of_respondents == 1:
            yes_by_all += len(responses)

        else:
            list_of_responses = group.split('\n')
            print("List of responses: ")
            print(list_of_responses)
            print("\n")

            for answer in list_of_responses[0]:
                occurences = 0
                print(answer)

                for response in list_of_responses:

                    if answer in response:
                        occurences += 1

                    else:
                        pass

                if occurences == number_of_respondents:
                    yes_by_all += 1

                else:
                    pass

        print(yes_by_all)
        print("\n")
        print("\n")
#            print("Answer: ")
#            print(i)
#            print("Count of letter prevalence: ")
#            print(group.count(i))

#            if group.count(i) == number_of_respondents and i not in already_checked :
#                yes_by_all += 1
#                already_checked.append(i)
#                print("Already checked: ")
#                print(already_checked)
#                print("Valid Answer: ")
#                print(yes_by_all)
#                print("\n")
#            else:
#                print("Valid Answer: ")
#                print(yes_by_all)
#                print("\n")
#                pass
#        print("\n\n")

    print(yes_by_all)

    return yes_by_all


customsdecl()
