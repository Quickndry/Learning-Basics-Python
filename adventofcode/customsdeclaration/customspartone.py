def customsdecl():
    unique_answer_count = []

    #Open Txt file and convert content to list
    with open('input.txt', encoding='utf-8') as file:
	       contents = file.read()
	       list_of_groups = contents.split('\n\n')

#    Testing ground
#    print("List of groups:")
#    print(list_of_groups)
#    print('\n')

    #Loop through groups inside list
    for group in list_of_groups:

        #Declare variables that are reset with every new group being looped
        list_of_all_answers = []
        final_answer_list =[]

        #Loop through every answer given in a group
        for answer in group:
            #Remove \n and add to new list
            list_of_all_answers.append(answer.strip())

            #Convert list to set so that duplicate answers are removed
            set_of_unique_answers = set(list_of_all_answers)]

#            Testing ground
#            print("Answer analyzed:")
#            print(answer)
#            print("List of unique answers:")
#            print(set_of_unique_answers)

        #Loop through every unique answer in set
        for unique_answer in set_of_unique_answers:

            #check if unique answer is ' ' so as to remove it
            if unique_answer:
                final_answer_list.append(unique_answer)
            else:
                pass

#        Testing ground
#        print("Final answer list: ")
#        print(final_answer_list)
#        print('\n')

        #Find number of unique answers given per group and append to list
        n_of_answers = len(final_answer_list)
        unique_answer_count.append(n_of_answers)

    #Sum number of unique answers given per group
    sum_of_answers = sum(unique_answer_count)

    print(sum_of_answers)
    return sum_of_answers


customsdecl()
