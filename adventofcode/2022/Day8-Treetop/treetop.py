def partone(inputfile):

    with open(inputfile, 'r') as file:
        fstring = file.read()

    n_columns = len(fstring.split('\n')[0]) - 1

    l_of_l = [list(x) for x in fstring.split('\n')]
    
    n_rows = len(l_of_l) - 1
#    print("Number of rows: ", n_rows, "\nNumber of ss: ", n_columns)
    
    visible_trees = 0 

    for ir, row in enumerate(l_of_l):
#        print("\nRow ID: ", ir)
        if ir == 0 or ir == n_rows:
            visible_trees += n_columns + 1
#            print("Visible Trees: ", visible_trees)

        else:
            for it, tree in enumerate(row):
#                print("\nTree height: ", tree)
                if it == 0 or it == n_columns:
                    visible_trees += 1
#                    print("Visible Trees: ", visible_trees)

                else:
                    isvisible = True
#                    print("Pre: ", row[0:it])
                    for othertree in row[0:it]:
                        if tree <= othertree:
                            isvisible = False
                            break

                    if isvisible == False:
                        isvisible = True
#                        print("After: ", row[it+1:])
                        for othertree in row[it+1:]:
                            if tree <= othertree:
                                isvisible = False
                                break

                        if isvisible == False:
                            isvisible = True
#                            print("COL Pre: ", [x[it] for x in l_of_l[:ir]])
                            for treerow in l_of_l[:ir]:
                                if tree <= treerow[it]:
#                                    print("treerow[it]: ", treerow[it], "\nIT: ", it)
                                    isvisible = False
                                    break

                            if isvisible == False:
#                                print("COL After: ", [x[it] for x in l_of_l[ir+1:]])
                                isvisible = True
                                for treerow in l_of_l[ir+1:]:
                                    if tree <= treerow[it]:
#                                        print("treerow[it]: ", treerow[it], "\nIT: ", it)
                                        isvisible = False
                                        break

                                if isvisible == True:
                                    visible_trees += 1
#                                    print("Visible Trees: ", visible_trees)
#                                else:
#                                    print("Tree not visible")
                            else:
                                visible_trees += 1
#                                print("Visible Trees: ", visible_trees)
                        else:
                            visible_trees += 1
#                            print("Visible Trees: ", visible_trees)
                    else:
                        visible_trees += 1
#                        print("Visible Trees: ", visible_trees)
    print(visible_trees)

def finddistance(tree, col_or_row):
    distance = 0
    for othertree in col_or_row:
        distance += 1
        if othertree >= tree:
            return distance
    return distance


def parttwo(inputfile):
    with open(inputfile, 'r') as file:
        fstring = file.read()
    
    rows = fstring.split('\n')
    
    rowlength = len(rows[0]) - 1
    columnlength = len(rows) - 1
    scenic_scores = []

    for ir, row in enumerate(rows):
        for it, tree in enumerate(row):
            bef_row = [x for x in row[:it]]
            aft_row = [x for x in row[it+1:]]
            bef_row.reverse()
            bef_col = [x[it] for x in rows[:ir]]
            aft_col = [x[it] for x in rows[ir+1:]]
            bef_col.reverse()
#            print("Bef row: ", bef_row, "Aft row: ", aft_row, "Bef col: ", bef_col, "Aft col: ", aft_col)

            if ir == 0 and it == 0:
                brdist = 0
                ardist = finddistance(tree, aft_row)
                bcdist = 0
                acdist = finddistance(tree, aft_col)
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)
            
            elif ir == 0 and it == rowlength:
                brdist = finddistance(tree, bef_row)
                ardist = 0
                bcdist = 0
                acdist = finddistance(tree, aft_col)
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)

            elif ir == columnlength and it == 0:
                brdist = 0
                ardist = finddistance(tree, aft_row)
                bcdist = finddistance(tree, bef_col)
                acdist = 0
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)

            elif ir == columnlength and it == rowlength:
                brdist = finddistance(tree, bef_row)
                ardist = 0
                bcdist = finddistance(tree, bef_col)
                acdist = 0
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)

            elif ir == 0:
                brdist = finddistance(tree, bef_row)
                ardist = finddistance(tree, aft_row)
                bcdist = 0
                acdist = finddistance(tree, aft_col)
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)

            elif ir == columnlength:
                brdist = finddistance(tree, bef_row)
                ardist = finddistance(tree, aft_row)
                bcdist = finddistance(tree, bef_col)
                acdist = 0
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)

            elif it == 0:
                brdist = 0
                ardist = finddistance(tree, aft_row)
                bcdist = finddistance(tree, bef_col)
                acdist = finddistance(tree, aft_col)
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)

            elif it == rowlength:
                brdist = finddistance(tree, bef_row)
                ardist = 0
                bcdist = finddistance(tree, bef_col)
                acdist = finddistance(tree, aft_col)
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)

            else:
                brdist = finddistance(tree, bef_row)
                ardist = finddistance(tree, aft_row)
                bcdist = finddistance(tree, bef_col)
                acdist = finddistance(tree, aft_col)
                scenic_score = bcdist * brdist * acdist * ardist
                scenic_scores.append(scenic_score)
                print("Row: ", ir, "Col: ", it, "Tree: ", tree, "Score: ", scenic_score)


    print("Max scene: ", max(scenic_scores))

#partone("input.txt")
parttwo("input.txt")

