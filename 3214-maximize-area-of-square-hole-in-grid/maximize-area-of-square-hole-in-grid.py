class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hx, hy, vx, vy, i = hBars[0], hBars[0], vBars[0], vBars[0], 0
        hBars.sort()
        vBars.sort()
        while i < len(hBars):
            tempx = hBars[i]
            while i < len(hBars) -1 and hBars[i] + 1 == hBars[i+1]:
                i+=1
            tempy = hBars[i]
            i+=1
            if tempy - tempx > hy - hx:
                hx, hy = tempx, tempy
        i = 0
        while i < len(vBars):
            tempx = vBars[i]
            while i < len(vBars) -1 and vBars[i] + 1 == vBars[i+1]:
                i+=1
            tempy = vBars[i]
            i+=1
            if tempy - tempx > vy - vx:
                vx, vy = tempx, tempy
        i = min(hy - hx + 2, vy - vx + 2)
        return i*i 