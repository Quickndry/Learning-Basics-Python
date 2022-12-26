def dic_size(dic, full_dic):
    size = 0
    for value in dic:
        if value.isdigit():
            size += int(value)
        else:
            size += dic_size(full_dic[value], full_dic)
    return size

def directory_analytics(inputfile, totlsize, upsize):
    with open(inputfile, 'r') as file:
        filestring = file.read()
    
    dir_rough = filestring.split('$ cd ')

    curr_path = []
    dir_dic = {}

    for dir in dir_rough:
        if dir == '':
            pass

        else:
            components = dir.split('\n')
            if components[0] == '..':
                curr_path = curr_path[0:-1]
                pass
            else:
                values = []
                curr_path.append(components[0])
                curr_p = '/'.join(curr_path)

                for component in components[1:]:

                    if component == '$ ls':
                        pass

                    else:
                        parts = component.split(' ')

                        if parts[0] == 'dir':
                            dir_p = '/'.join(curr_path) + "/" + parts[1]
                            values.append(dir_p)

                        elif parts[0] == '':
                            pass
                        else:
                            values.append(parts[0])
                dir_dic[curr_p] = values

    dsize_dic = {}
    for key in dir_dic.keys():
        dirsize = dic_size(dir_dic[key], dir_dic)
        dsize_dic[key] = dirsize


    unused_space = totlsize - dsize_dic['/']
    leftover_upd = upsize - unused_space
    poss_drives = []
    for key in dsize_dic.keys():
        if dsize_dic[key] > leftover_upd:
            poss_drives.append(dsize_dic[key])
    poss_drives.sort()
    print(poss_drives[0])

directory_analytics('input.txt', 70000000, 30000000)