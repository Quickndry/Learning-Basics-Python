#works fine

def arrange(s):
    t = []
    firstdigit = 0
    seconddigit = len(s) - 1
    reverse = 1
    x = int(len(s)/2)*2

    if x == len(s): #if length of s is even
        while len(t) < len(s):
        
            if reverse == 1:
                t.append(s[firstdigit])
                t.append(s[seconddigit])
                reverse = 0
        
            elif reverse == 0:
                t.append(s[seconddigit])
                t.append(s[firstdigit])
                reverse = 1
        
            firstdigit += 1
            seconddigit -= 1
    
    else:  # if length of s is odd
        while len(t) < len(s):
            if firstdigit == seconddigit:
                t.append(s[firstdigit])
                break
            
            if reverse == 1:
                t.append(s[firstdigit])
                t.append(s[seconddigit])
                reverse = 0

            elif reverse == 0:
                t.append(s[seconddigit])
                t.append(s[firstdigit])
                reverse = 1

            firstdigit += 1
            seconddigit -= 1
    
    return t

