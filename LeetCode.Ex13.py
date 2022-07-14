def RomanToInt(s):
    lis = list(s)
    sum=0
    for i in range(len(lis)):
        if lis[i] == 'I':
            sum += 1
        elif lis[i] == 'V':
            if lis[i-1] != "I" or i == 0:
                sum += 5
            else:
                sum += 3
        elif lis[i] == 'X':
            if lis[i-1] != "I" or i == 0:
                sum += 10
            else:
                sum += 8
        elif lis[i] == 'L':
            if lis[i-1] != "X" or i == 0:
                sum += 50
            else:
                sum += 30
        elif lis[i] == 'C':
            if lis[i-1] != "X" or i == 0:
                sum += 100
            else:
                sum += 80
        elif lis[i] == 'D':
            if lis[i-1] != "C" or i == 0:
                sum += 500
            else:
                sum += 300
        elif lis[i] == 'M':
            if lis[i-1] != "C" or i == 0:
                sum += 1000
            else:
                sum += 800
        print(sum)
RomanToInt("CDLXIX")