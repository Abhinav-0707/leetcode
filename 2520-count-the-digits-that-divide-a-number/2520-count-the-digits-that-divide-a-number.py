class Solution(object):
    def countDigits(self, num):
        org = num
        count = 0
        while num > 0:
            digit = num % 10
            if digit != 0 and org % digit == 0:
                count += 1
            num //= 10
        return count
