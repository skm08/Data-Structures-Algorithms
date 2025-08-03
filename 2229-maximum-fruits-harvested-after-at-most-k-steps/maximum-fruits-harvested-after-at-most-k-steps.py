class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        n = len(fruits)

        # Step 2: Initialize pointers and variables
        left = right = 0
        currFruits = maxFruits = 0

        # Step 3: Expand the window to the right
        while right < n:
            currFruits += fruits[right][1]

            # Step 4 and Step 5: Shrink from left if window is unreachable
            while left <= right and not self.canReach(fruits, left, right, startPos, k):
                currFruits -= fruits[left][1]
                left += 1  # shrink window

            # Step 6: Update max fruits collected
            maxFruits = max(maxFruits, currFruits)
            right += 1  # Step 7: Expand to next position

        # Step 8: Return result
        return maxFruits

    # Step 4 Helper: Check if the current window is reachable in k steps
    def canReach(self, fruits, left, right, startPos, k):
        leftPos = fruits[left][0]
        rightPos = fruits[right][0]

        minSteps = min(abs(startPos - leftPos) + (rightPos - leftPos),
                       abs(startPos - rightPos) + (rightPos - leftPos))

        return minSteps <= k 