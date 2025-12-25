class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        TotHappiness = 0
        for turn in range(k):
            UValue = happiness[turn] - turn
            if UValue <= 0:
                break
            TotHappiness+=UValue
        return TotHappiness

        