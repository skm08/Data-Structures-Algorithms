class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        time = []
        for meeting in meetings:
            time.append((meeting[0], 1))
            time.append((meeting[1] + 1, 0))
        
        # Sort the time list
        time.sort()
        
        # Apply Line-Sweep 1D
        overlap = 0
        count = time[0][0] - 1  # Count free time before start
        for i in range(len(time) - 1):
            if time[i][1] == 0:
                overlap -= 1
            else:
                overlap += 1
            
            if overlap == 0:
                count += time[i + 1][0] - time[i][0]
        
        count += days - time[-1][0] + 1  # Count free time after end
        return count