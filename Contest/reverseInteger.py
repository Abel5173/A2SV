class Solution:
    def reverse(self, x: int) -> int:
        for i in range(len(str(x))):
            if str(x)[i] != '0':
                break
        x = str(x)[i:]
        if x[0] == '-':
            x = '-' + x[1:][::-1]
        else:
            x = x[::-1]
        x = int(x)
        if x < -2**31 or x > 2**31-1:
            return 0
        return x