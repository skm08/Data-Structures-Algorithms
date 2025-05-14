class Solution:
    def lengthAfterTransformations(self, s: str, t: int, n: List[int]) -> int:
        A = 26 
        Z = 10**9 + 7 

        def f(a, b): 
            d = [[0] * A for _ in range(A)] 
            for i in range(A):
                for j in range(A):
                    v = 0 
                    for l_loop in range(A): 
                        v = (v + a[i][l_loop] * b[l_loop][j]) % Z
                    d[i][j] = v
            return d

        def g(a, e): 
            p = [[0] * A for _ in range(A)] 
            for i in range(A):
                p[i][i] = 1 

            q = a 
            while e > 0:
                if e % 2 == 1:
                    p = f(p, q) 
                q = f(q, q) 
                e //= 2
            return p

        if t == 0:
            return len(s)

        x = [[0] * A for _ in range(A)] 
        for r in range(A): 
            h = n[r] 
            for k in range(h): 
                j = (r + k + 1) % A
                x[r][j] = 1
        
        y = g(x, t) 

        l = [0] * A 
        for r in range(A): 
            v = 0 
            for c_col in range(A): 
                v = (v + y[r][c_col]) % Z
            l[r] = v
            
        o = 0 
        for i_char in s: 
            j_code = ord(i_char) - ord('a')
            o = (o + l[j_code]) % Z
            
        return o