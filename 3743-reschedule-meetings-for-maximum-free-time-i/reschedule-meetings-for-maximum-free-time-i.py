from collections import deque

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        if eventTime > endTime[-1]:
            startTime.append(eventTime)
            endTime.append(eventTime)
        
        n = len(startTime)
        max_sum = 0
        win_sum = 0
        pos = 0
        last_end = 0
        dq = deque()
        
        while pos < n:
            win_sum += (startTime[pos] - last_end)
            dq.append(startTime[pos] - last_end)
            max_sum = max(max_sum, win_sum)
            if len(dq) > k:
                win_sum -= dq.popleft()
            last_end = endTime[pos]
            pos += 1
        return max_sum