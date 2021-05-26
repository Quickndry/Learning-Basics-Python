def duplicate_encode(word):
    stringinput = word.lower()
    lstoutput = []
    strnglist = [char for char in stringinput]
    for i in strnglist:
        if strnglist.count(i) > 1:
            lstoutput.append(')')
        else:
            lstoutput.append('(')
    fstrng = ''.join(lstoutput)
    return fstrng
