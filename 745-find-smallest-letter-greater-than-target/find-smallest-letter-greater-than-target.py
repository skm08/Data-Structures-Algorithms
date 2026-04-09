class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target: 
            return letters[0]
            
        lft, rgt = 0, len(letters) - 1
        while lft < rgt:
            mid= (lft + rgt)//2
            if letters[mid] <= target:
                lft = mid+1
            else:
                rgt = mid 
        return letters[rgt] 