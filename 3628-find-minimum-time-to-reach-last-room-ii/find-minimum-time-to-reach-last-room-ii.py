class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        M, N = len(moveTime), len(moveTime[0])
        minH = [(0,0,0,True)] # t,x,y,isOdd
        visit = set()
        while minH:
            t, x, y, isOdd = heapq.heappop(minH)
            if (x,y) == (M-1,N-1):
                return t
            for dx, dy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0 <= dx < M and 0 <= dy < N and (dx, dy) not in visit:
                    visit.add((dx,dy))
                    add = 1 if isOdd else 2
                    heapq.heappush(minH,(max(moveTime[dx][dy],t) + add ,dx,dy,not isOdd))
        return