class Solution(object):
    def fib(self, n):
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Recursive call
        return self.fib(n - 1) + self.fib(n - 2)