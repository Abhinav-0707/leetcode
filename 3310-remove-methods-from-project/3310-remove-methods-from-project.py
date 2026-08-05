class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods (reachable from k)
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if not suspicious[nei]:
                    suspicious[nei] = True
                    stack.append(nei)

        # Check if any outside method invokes a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return remaining methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans