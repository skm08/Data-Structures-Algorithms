class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        number = "1"
        for _ in range(2, n + 1):
            res = []
            count = 1
            curr = number[0]
            for j in range(1, len(number)):
                if number[j] == curr:
                    count += 1
                else:
                    res.append(str(count) + curr)
                    curr = number[j]
                    count = 1
            res.append(str(count) + curr)
            number = "".join(res)
        return number