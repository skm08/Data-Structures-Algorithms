class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = float('inf')
        used = []
        found = False
        for i in freq:
            
            while freq[i] >= 3:
                found = True
                a = b = c = -1
                for j in range(len(nums)):
                    
                    if nums[j] == i and j not in used:
                        if a == -1 :
                            a = j
                            used.append(j)
                        elif b == -1: 
                            b = j
                        elif c == -1: 
                            c = j 
                            break
                currMin = abs(a - b) + abs(b - c) + abs(c - a)

                if currMin < res: res = currMin
                freq[i] -= 1
        return res if found else -1