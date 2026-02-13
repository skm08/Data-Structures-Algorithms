from collections import defaultdict


class Solution:
    def check(self, s: str, x: str, y: str, z: str) -> int:
        maxi = 0
        n = len(s)
        count_x = 0
        count_y = 0
        mp = {0: -1}

        for i in range(n):
            if s[i] == z:
                mp.clear()
                mp[0] = i
                count_x = 0
                count_y = 0
            if s[i] == x:
                count_x += 1
            if s[i] == y:
                count_y += 1
            diff = count_x - count_y
            if diff in mp:
                maxi = max(maxi, i - mp[diff])
            else:
                mp[diff] = i
        return maxi

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # one character
        ans = 1
        ch = s[0]
        last = 0

        for i in range(1, n):
            if s[i] == ch:
                ans = max(ans, i - last + 1)
            else:
                ch = s[i]
                last = i

        # two characters
        ans = max(ans, self.check(s, "a", "b", "c"))
        ans = max(ans, self.check(s, "b", "c", "a"))
        ans = max(ans, self.check(s, "c", "a", "b"))

        # three characters
        mp = {(0, 0): -1}
        count_a = count_b = count_c = 0

        for i, char in enumerate(s):
            if char == "a":
                count_a += 1
            elif char == "b":
                count_b += 1
            elif char == "c":
                count_c += 1

            diff1 = count_a - count_b
            diff2 = count_a - count_c
            key = (diff1, diff2)

            if key in mp:
                ans = max(ans, i - mp[key])
            else:
                mp[key] = i

        return ans