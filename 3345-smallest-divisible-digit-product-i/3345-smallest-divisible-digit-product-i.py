class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            product = 1

            for digit in str(n):
                product *= int(digit)

            if product % t == 0:
                return n

            n += 1