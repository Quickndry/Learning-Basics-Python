def move_zeros(lst):
    adapted_lst = [x for x in lst if x != 0]
    zeroes_lst = [x for x in lst if x not in adapted_lst]
    adapted_lst.extend(zeroes_lst)
    return adapted_lst