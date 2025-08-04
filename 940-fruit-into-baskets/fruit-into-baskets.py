class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        max_count = left = 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left+=1
            max_count = max(max_count,right-left+1)
        return max_count