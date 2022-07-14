class Solution:
    def myAtoi(self, s: str) -> int:
        lst = [x for x in s]
        num = 0
        ans = []
        brk = 'false'
        sign=''
        for i in range(len(lst)):
            if lst[i] == ' ' and num == 0:
                pass
            elif lst[i] == '+' and num == 0:
                sign = 'plus'
                num = 1
            elif lst[i] == '-' and num == 0:
                sign = 'minus'
                num = 1
            elif lst[i].isdigit():
                num = 1
                ans.append(lst[i])
            else:
                break
        if len(ans) == 0:
            return 0
        mult = 1
        res = 0
        for i in range(len(ans)-1,-1,-1):
            res += int(ans[i]) * mult
            mult *= 10
        if sign == 'minus':
            if res > 2147483648:
                return 0 - 2147483648
            else:
                return 0 - res
        else:
            if res >= 2147483648:
                return 2147483647
            else:
                return res
                