def customsdecl():
    yes_by_all = 0

    #Open Txt file and convert content to list
    with open('input.txt', encoding='utf-8') as file:
	       contents = file.read()
	       list_of_groups = contents.split('\n\n')
#    print(list_of_groups)

    #Loop through groups inside list
    for group in list_of_groups:
        number_of_respondents = len(group.split())

        #If only one respondent, all their answers are valid
        if number_of_respondents == 1:
            yes_by_all += len(group)

        #If multiple respondents
        else:
            #Split group into individual respondents
            list_of_responses = group.split('\n')

            #Loop through answers given by first respondent
            for answer in list_of_responses[0]:

                #Count answer in group and compare with number of respondents.
                if group.count(answer) == number_of_respondents:
                    yes_by_all += 1

                else:
                        pass

    print(yes_by_all)
    return yes_by_all


customsdecl()
