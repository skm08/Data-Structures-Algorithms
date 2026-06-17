class Solution:
    def processStr(self, s: str, k: int) -> str:
        str_len = 0
        for i in s:
            if i.islower():
                str_len += 1
            elif i == '*' and str_len > 0:
                str_len -= 1

            elif i == '#':
                str_len *= 2

        if k >= str_len or k < 0:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.islower():
                str_len -= 1
                if k == str_len:
                    return ch

            elif ch == '#':
                str_len //= 2
                if k >= str_len:
                    k -= str_len

            elif ch == '*':
                str_len += 1

            elif ch == '%':
                k = str_len - k - 1

                

        
        