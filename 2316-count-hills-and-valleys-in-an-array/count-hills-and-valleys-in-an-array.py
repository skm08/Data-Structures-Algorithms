class Solution:
    def countHillValley(self, n: List[int]) -> int:
        m=0 # taking m as left index 
        s=0 # s as count
        for i in range(1,len(n)-1):
            if n[i]!=n[i+1]:
                if n[i]>n[m] and n[i]>n[i+1]:
                    s+=1
                elif n[i]<n[m] and n[i]<n[i+1]:
                    s+=1
                m=i
        return s