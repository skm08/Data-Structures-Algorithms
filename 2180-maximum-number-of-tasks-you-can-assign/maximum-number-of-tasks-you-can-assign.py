class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        l, r = 0, min(len(workers), len(tasks))
        tasks.sort()
        workers.sort()
        def can_finish_tasks(m, pills):
            q = deque()
            i = 0
            n = len(workers)

            for j in range(n-m, n):
                w = workers[j]
                while i < m and tasks[i] <= w + strength:
                    q.append(tasks[i])
                    i += 1
                if not q:
                    return False
                if q[0] <= w:
                    q.popleft()
                else :
                    if not pills:
                        return False
                    pills -= 1
                    q.pop()
            return True

        while l < r:
            m = (l + r + 1)//2
            if can_finish_tasks(m, pills):
                l = m
            else:
                r = m-1
        return l
        