def string_split(string):
    string_list = string.split(' ')
    string_join_list = []
    fin_list = []
    cur_list = []
    string_chunk = 0
    for item in string_list:
        string_chunk += len(item)
        if string_chunk < 50:
            string_join_list.append(item)
        else:
            string_join_list.append('\n')
            string_chunk = 0
    string_join_list.append(item)
    for item in string_join_list:
        if item != '\n':
            cur_list.append(item)
        else:
            fin_list.append(cur_list)
            cur_list = []

    fin_list.append(cur_list)
    cur_list = []

    for item in fin_list:
        cur_result = ' '.join(item)
        cur_list.append(cur_result)

    result = '\n'.join(cur_list)
    return result





