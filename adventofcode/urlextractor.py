import re

def domain_name(url):
    print(url)
    urlcontent = re.split('[/.]', url)
    print(urlcontent) #creates URL components list
    splist = urlcontent[:len(urlcontent)//2]
    splisttwo = urlcontent[len(urlcontent)//2:]
    print(splist) #creates new list out of first halve
    possurl = max(splist, key=len)
    if possurl == 'http:' or 'https:':
			#if possurl not found in first halve, try second halve
    	possurl = max(splisttwo, key=len)
    print(possurl) #takes the longest word and hopes it's a url
    return possurl
