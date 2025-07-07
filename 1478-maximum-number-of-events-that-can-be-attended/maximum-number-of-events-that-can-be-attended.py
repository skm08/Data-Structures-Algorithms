class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq=[]
        i,n,ans=0,len(events),0
        mxday=max(i[1] for i in events)
        for day in range(1,mxday+1):
            while i<n and events[i][0]<=day:
                heapq.heappush(pq,events[i][1])
                i+=1
            while pq and day>pq[0]:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans+=1
        return ans