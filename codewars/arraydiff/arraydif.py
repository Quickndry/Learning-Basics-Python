# Your goal in this kata is to implement a difference function, which 
# subtracts one list from another and returns the result.
# 
# It should remove all values from list a, which are present in list b.
# 
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed 
# from the other:
# 
# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a, b):
    new_array =[]

    for x in a:
        if x in b:
            pass
        else:
            new_array.append(x)

    
    print(new_array)
    return new_array

array_diff([-9, -14, -1, 20, 8, -15, -5, 8, -10, 0, -10, 13, 17, 19, -20, 4, 9],[-8, -15, -19, -18, -8])
