def remove_parentheses(s):
    start_par = '('
    end_par = ')'
    
    stack = []
    new_sentence = []
    
    for i in s:
        if i == start_par:
            stack.append(i)
        if not stack:
            new_sentence.append(i)
        if i == end_par:
            stack.pop()
    return ''.join(new_sentence)
