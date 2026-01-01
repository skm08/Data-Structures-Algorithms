class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        bricks: dict[str, list[str]] = dict()
        memo: dict[str, bool] = dict()
        for brick in allowed:
            if brick[:2] not in bricks: bricks[brick[:2]] = []
            bricks[brick[:2]].append(brick[-1])
        def dfs(bottom: str) -> bool:
            if len(bottom) == 1: return True
            elif memo.get(bottom): return memo.get(bottom)
            next_rows: list[str] = []
            reconstruct(bottom, 0, [], next_rows)
            for row in next_rows:
                if dfs(row):
                    memo[bottom] = True
                    return True
            memo[bottom] = False
            return False
        def reconstruct(bottom: str, i: int, cur: list[str], next_rows: list[str]) -> None:
            if i + 1 == len(bottom):
                next_rows.append(''.join(cur))
                return
            if bottom[i:i + 2] not in bricks: return
            for brick in bricks[bottom[i:i + 2]]:
                cur.append(brick)
                reconstruct(bottom, i + 1, cur, next_rows)
                cur.pop()
        return dfs(bottom)