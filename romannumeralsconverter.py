class RomanNumeralsConverter:
    dictromannum = {0:'',
        1:'I', 2:'II', 3:'III', 4:'IV', 5:'V',
        6:'VI', 7:'VII', 8:'VIII', 9:'IX',
        10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L',
        60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',
        100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D',
        600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
        1000:'M', 2000:'MM', 3000:'MMM'}

    dictnum = {'I':1, 'V':5,
        'X':10, 'L':50,
        'LX':60, 'LXX':70, 'LXXX':80, 'XC':90,
        'C':100, 'CC':200, 'CCC':300, 'CD':400, 'D':500,
        'DC':600, 'DCC':700, 'DCCC':800, 'CM':900,
        'M':1000, 'MM':2000, 'MMM':3000}

    negdictnum = {'IV':4, 'IX':9,
        'XL':40, 'XC':90,
        'CD':400, 'CM':900}

    def to_roman(inp, dic = dictromannum):
        n = 0
        inps = str(inp)
        newlist = [char for char in inps[::-1]]
        digitlist = []
        for index, variable in enumerate(newlist):
            x = variable + '0' * index
            digitlist.append(int(x))
        romlist = [dic.get(n, n) for n in digitlist]
        romlist.reverse()
        romnum = ''.join(romlist)
        return romnum

    def from_roman(inp, negdic = negdictnum, dic = dictnum):
        d = 2
        inplist = [inp[i:i+d] for i in range(0, len(inp), d)]
        newlist = [negdic.get(n, n) for n in inplist]
        strlist = [str(x) for x in newlist]
        numstring = ''.join(strlist)
        numlist = [dic.get(n, n) for n in numstring]
        intlist = [int(n) for n in numlist]
        romnum = sum(intlist)
        return romnum
