class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, remaining):

            # Found a valid combination
            if remaining == 0:
                result.append(current[:])
                return

            # Sum exceeded target
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Choose
                current.append(candidates[i])

                # Explore
                # Use i again because numbers can be reused
                backtrack(i, current, remaining - candidates[i])

                # Undo choice
                current.pop()

        backtrack(0, [], target)

        return result