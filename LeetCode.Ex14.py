def longestCommonPrefix(strs:list)->str:
    prefix = ""
    lists = []
    index = 0
    length = 100
    for i in range(len(strs)):
        lists.append(list(strs[i]))
    for i in range(len(lists)):
        if len(lists[i]) < length:
            length = len(lists[i])
            index = i
    for i in range(len(lists[index])): #will iterate through the smallest of lists
        char = lists[index][i]
        for j in range(len(lists)): #will iterate through the big list
            if len(lists[j]) <= i:
                break
            elif lists[j][i] == char:
                pass
            else:
                return prefix
        prefix = prefix + char
    return prefix