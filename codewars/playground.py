
# CAN BE DELETED

# a function that seeks to extract the domain name from full URLs.

import re

def domain_name(url):
    print(url)
    
    urlComponents = ["http:", "https:", "www", "com", "net", "tv", "php", "info", "error", "img", "index", "edu", "warez", "co", "uk", "jp", "ru", "org", "br", "us", "it", "de", "es", "eu"]

    urlContent = re.split('[/.]', url)

    domainList = [x for x in urlContent if x not in urlComponents]
    
    try:
        domain = domainList[1]
    except:
        domain = domainList[0]
        
    print(domainList)
    print(domain)
    
    return(domain)




import re

def domain_name(url):
    print(url)
    urlcontent = re.split('[/.]', url)
    print(urlcontent) #creates URL components list
    
    splist = urlcontent[:len(urlcontent)//2]
    splisttwo = urlcontent[len(urlcontent)//2:]
    print(splist) #creates new list out of first halve
    
    possurl = max(splist, key=len) 
    print(type(possurl))
    print(possurl) #takes longest word and hope's its a URL
    
    if possurl == "http:" or "https:":
		#if possurl not found in first halve, try second halve
        possurl = max(splisttwo, key=len)
        print(possurl) #takes the longest word and hopes it's a url

    else:
        pass
    
    return possurl