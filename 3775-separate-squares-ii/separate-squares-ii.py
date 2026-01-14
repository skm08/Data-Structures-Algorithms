class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        sweepEvents = []
        for xStart, yStart, sideLength in squares:
            sweepEvents.append((yStart, 1, xStart, xStart + sideLength))          # Square starts
            sweepEvents.append((yStart + sideLength, -1, xStart, xStart + sideLength))  # Square ends
        sweepEvents.sort()
        activeIntervals = []
        previousY = sweepEvents[0][0]
        totalArea = 0
        areaSegments = []
        def calculateUnionWidth(intervals):
            intervals.sort()
            totalWidth = 0
            currentEnd = -10**30
            for left, right in intervals:
                if left > currentEnd:
                    totalWidth += right - left
                    currentEnd = right
                elif right > currentEnd:
                    totalWidth += right - currentEnd
                    currentEnd = right
            return totalWidth
        for currentY, eventType, xLeft, xRight in sweepEvents:
            if currentY > previousY and activeIntervals:
                height = currentY - previousY
                width = calculateUnionWidth(activeIntervals)
                areaSegments.append((previousY, height, width))
                totalArea += height * width
            if eventType == 1:
                activeIntervals.append((xLeft, xRight))
            else:
                activeIntervals.remove((xLeft, xRight))
            previousY = currentY
        halfArea = totalArea / 2
        accumulatedArea = 0
        for startY, segmentHeight, segmentWidth in areaSegments:
            segmentArea = segmentHeight * segmentWidth
            if accumulatedArea + segmentArea >= halfArea:
                return startY + (halfArea - accumulatedArea) / segmentWidth
            accumulatedArea += segmentArea
        return 0.0