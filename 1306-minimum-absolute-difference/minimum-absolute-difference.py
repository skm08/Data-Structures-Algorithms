class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        return arr.sort() or [
            [a,b]  for i,(a,b) in enumerate(pairwise(arr))
            if (i==0 and (m:= min(y-x for x,y in pairwise(arr))) <0) or (b-a)==m
        ]