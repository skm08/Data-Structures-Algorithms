class Solution:
    def kthCharacter(self, k: int) -> str:
        n=1
        a="a"
        while n<k:
            for i in range(n):
                a+=chr(ord(a[i])+1)
            n*=2
        print(a)
        return a[k-1]
            