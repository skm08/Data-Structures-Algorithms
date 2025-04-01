class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        mem = [-1] * n
        
        def findMaxPoints(pos):
            if pos >= n:
                return 0
            if mem[pos] != -1:
                return mem[pos]
            
            exclude = findMaxPoints(pos + 1)
            include = questions[pos][0] + findMaxPoints(pos + questions[pos][1] + 1)
            mem[pos] = max(exclude, include)
            return mem[pos]
        
        return findMaxPoints(0)