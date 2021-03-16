# a function that seeks to extract the domain name from full URLs.

import re

def domain_name(url):
    print(url)
    
    fullstopElements = []
    dashElements = []


    counter = 0

    for i in url:
        counter += 1
        if i == '.':
            fullstopElements.append(counter)
        elif i == '/':
            dashElements.append(counter + 1)
        else:
            pass
    
    
    if 'www' in url:
        domain = url[fullstopElements[0]:fullstopElements[1] - 1] 
    elif 'http' in url:
        domain = url[dashElements[0]:fullstopElements[0] - 1]
    else:
        domain = url[:fullstopElements[0] - 1]
    
    print(domain)
    return(domain)