class Solution:
    def minFlips(self, s: str) -> int:
        res = inf
        for v in 0,1:
            res = min(res,q:=sum(map(ne,s,cycle(f'{v}{v^1}'))))
            if len(s)&1: res = min(res,min(accumulate(zip(s,cycle(f'{v^1}{v}')),
                lambda q,p:q-eq(*p)+ne(*p),initial=q)))

        return res