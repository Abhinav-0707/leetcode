class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]

        for ch in s:
            if ch == '(':
                # Start a new level
                stack.append(0)
            else:
                # Get the score inside the current ()
                inner = stack.pop()

                # () = 1
                # (A) = 2 * A
                score = max(2 * inner, 1)

                # Add score to the previous level
                stack[-1] += score

        return stack[0]