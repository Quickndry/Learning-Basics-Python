def generate_hashtag(s):
    hash = '#'
    tag = ''

    newlist = []
    if ' ' in s:

        wordlist = s.split(' ')
        print(wordlist)
        for i in wordlist:

            newlist.append(i.capitalize())
        print(newlist)
        tag = ''.join(newlist)
        print(tag)
    else:

        tag = s.capitalize()
        print(tag)
