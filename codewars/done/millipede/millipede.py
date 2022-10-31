def next_path(some_key, some_value, some_dict):
    placeholder_dict = some_dict.copy()
    del placeholder_dict[some_key]
    print("Placeholder Dictionary: ", placeholder_dict)
    if len(placeholder_dict) == 0:
        return True
    for ktwo, vtwo in placeholder_dict.items():
        if some_value[1] == vtwo[0]:
            placeholder = next_path(ktwo, vtwo, placeholder_dict)
            print("Placeholder: ", placeholder)
            if placeholder == True:
                return True
    return False

def solution(arr):
    print("Input: ", arr)
    word_dict = {k:[v[0], v[-1]] for k, v in enumerate(arr)}
    print("Word dictionary:  ", word_dict, "Word dict type: ", type(word_dict))
    for k, v in word_dict.items():
        ph = next_path(k, v, word_dict)
        if ph == True:
            return True
    return False


