# works fine
import re
def travel(r, zipcode):
    dict_of_addresses = {}

    # disect r to obtain list of addresses
    list_of_addresses = r.split(',')

    # create a list for postcodes, street numbers and rest of address

    list_of_postcodes = []
    list_of_streetnum = []
    list_of_streetnam = []

    for x in list_of_addresses:
        endpoint = len(x)
        startpoint = endpoint - 8
        postcode = x[startpoint:endpoint]
        list_of_postcodes.append(postcode)


        streetnumber = re.search('^([0-9]){1,5}', x)
        list_of_streetnum.append(streetnumber.group())

        streetname = re.search('([a-zA-Z\.\s]){1,}', x)
        list_of_streetnam.append(streetname.group()[1:-4])

    # use zipcode to create output
    streetnumbers = ''
    streetnames = ''
    for i, postcode in enumerate(list_of_postcodes):
        if postcode[1:] == zipcode:
            streetnumbers += list_of_streetnum[i]
            streetnumbers += ','
            streetnames += list_of_streetnam[i]
            streetnames += ','
    
    output_string = zipcode + ':' + streetnames[0:-1] + '/' + streetnumbers[0:-1]
    return output_string
