class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        prefix = 0
        n = len(nums)
        res = n
        dic = {0 : -1}
        cur = 0
        for i in range(n):
            cur = (cur + nums[i]) % p
            need = (cur - target) % p
            if need in dic:
                res = min(res, i - dic[need])
            dic[cur] = i
        return res if res < n else -1