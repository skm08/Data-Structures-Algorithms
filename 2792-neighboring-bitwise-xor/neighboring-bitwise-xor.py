class Solution:
    def doesValidArrayExist(self, derived):
        res = 0
        for ele in derived:
            res ^= ele
        return res == 0