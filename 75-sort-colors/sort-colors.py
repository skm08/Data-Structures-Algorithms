class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)

        x = [0] * red
        y = [1] * white
        z = [2] * blue

        sorted_nums = x+y+z
        for i in range(len(sorted_nums)):
            nums[i] = sorted_nums[i]