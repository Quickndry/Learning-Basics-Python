# ---------------------------------------------------
# First round - successful ; Second round - too slow
# ---------------------------------------------------
# def parts_sums(ls):
#     newList = []
#     counter = len(ls)
# 
#     while counter > 0:
#         sumVal = sum(ls)
#         newList.append(sumVal)
#         del ls[0]
#         counter -= 1
#     newList.append(0)
#     print(newList)
#     return newList

def parts_sums(ls):
    newList = []
    sumVal = sum(ls)
    newList.append(sumVal)

    for i in ls:
        sumVal = sumVal - i
        newList.append(sumVal)

    return newList

ls = [1, 2, 3, 4, 5, 6]
parts_sums(ls)