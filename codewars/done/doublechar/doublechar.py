# In this Kata, you will write a function doubles that will remove double string characters that are adjacent to each other.

# For example:

# doubles('abbcccdddda') = 'aca', because, from left to right:

# a) There is only one 'a' on the left hand side, so it stays.
# b) The 2 b's disappear because we are removing double characters that are adjacent. 
# c) Of the 3 c's, we remove two. We are only removing doubles. 
# d) The 4 d's all disappear, because we first remove the first double, and again we remove the second double.
# e) There is only one 'a' at the end, so it stays.

# Two more examples: doubles('abbbzz') = 'ab' and doubles('abba') = "". In the second example, when we remove the b's in 'abba', the double a that results is then removed.



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def doubles(s):
#     print("Sentence: ", s)
# 
#     placeholder = ""
#     counter = -1
#     originalLength = len(s)
# 
#     for i in s:
#         counter += 1
# 
#         if i == placeholder:
#             s = s[:counter - 1] + s[counter + 1:]
#             break
# 
#         else:
#             placeholder = i
# 
#     if counter < originalLength - 1:
#         print(doubles(s))
#         return doubles(s)
#    
#     else:
#         print(s)
#         return s


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def doubles(s):
    for i in s:
        s = s.replace(i*2, "")
    return s

doubles("abbbzz")
