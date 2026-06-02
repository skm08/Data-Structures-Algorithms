class Solution:
    def earliestFinishTime(self, lS: List[int], lD: List[int], wS: List[int], wD: List[int]) -> int:
        mwE = min(wS[i]+wD[i] for i in range(len(wS)))
        mlE = min(lS[i]+lD[i] for i in range(len(lS)))
        return  min(min(
            max(ls, mwE) +ld
            for ls,ld in zip(lS,lD)
        ), min(
            max(ws, mlE) +wd
            for ws,wd in zip(wS,wD)
        ))
        