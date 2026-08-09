class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, M):
            # Can take all remaining piles
            if i >= n:
                return 0

            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                # Total remaining stones - opponent's maximum
                current = suffix[i] - solve(
                    i + X,
                    max(M, X)
                )

                best = max(best, current)

            dp[(i, M)] = best
            return best

        return solve(0, 1)