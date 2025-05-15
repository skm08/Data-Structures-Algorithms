class Solution:
    def getLongestSubsequence(self, w, g):        
        return [w[i] for i in range(len(w)) if i == 0 or g[i]!=g[i-1]]