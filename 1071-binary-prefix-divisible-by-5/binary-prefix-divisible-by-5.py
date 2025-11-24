class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        bin_str = ""
        out_arr = []

        i = 0
        while(i < len(nums)):


            bin_str += str(nums[i])

            if(int(bin_str, 2) % 5 == 0):
                out_arr.append(True)
            else:
                out_arr.append(False)

            i += 1

        return out_arr