from typing import List
from collections import defaultdict

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.arr1 = nums1
        self.arr2 = nums2.copy()
        self.ele_freq = defaultdict(int)
        for ele in nums2:
            self.ele_freq[ele] += 1
    
    def add(self, index: int, val: int) -> None:
        old_val = self.arr2[index]
        self.ele_freq[old_val] -= 1
        self.arr2[index] += val
        new_val = self.arr2[index]
        self.ele_freq[new_val] += 1
    
    def count(self, tot: int) -> int:
        res = 0
        for ele in self.arr1:
            target = tot - ele
            res += self.ele_freq.get(target, 0)
        return res