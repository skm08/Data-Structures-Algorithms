class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            ls = sum(nums[:i])
            rs = sum(nums[i+1:])
            answer.append(abs(ls-rs))
        return answer