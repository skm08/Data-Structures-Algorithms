class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def get_sum_array(arr):
            sum_arr = []
            for i in range(1, len(arr)):
                sum_arr.append(arr[i] + arr[i - 1])
            return sum_arr

        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        valid_array = is_non_decreasing(nums)
        operations = 0

        while not valid_array:
            sum_arr = get_sum_array(nums)
            smallest = min(sum_arr)
            index_of_smallest = sum_arr.index(smallest)
            nums = nums[:index_of_smallest] + [smallest] + nums[index_of_smallest + 2 :]
            valid_array = is_non_decreasing(nums)
            operations += 1

        return operations
