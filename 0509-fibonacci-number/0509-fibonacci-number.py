class Solution(object):
    def fib(self, n):
        # Base cases
        if n == 0 or n==1:
            return n
        # Recursive call
        return self.fib(n - 1) + self.fib(n - 2)