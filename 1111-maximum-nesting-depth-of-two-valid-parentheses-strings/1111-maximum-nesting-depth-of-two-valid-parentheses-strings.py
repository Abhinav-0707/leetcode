class Solution(object):
    def maxDepthAfterSplit(self, seq):
        depth = 0
        answer = []

        for ch in seq:
            if ch == '(':
                depth += 1
                answer.append(depth % 2)
            else:
                answer.append(depth % 2)
                depth -= 1

        return answer