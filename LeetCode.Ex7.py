class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = 'minus'
        else:
            sign = 'plus'
        x = abs(x)
        lst = [int(x) for x in str(x)]
        lst = lst[::-1]
        mult = 1
        ans = 0
        for i in range(len(lst)-1,-1,-1):
            ans += lst[i] * mult
            mult *= 10
        if ans > 2147483648:
            return 0
        elif sign == 'minus':
            return 0 - ans
        else:
            return ans