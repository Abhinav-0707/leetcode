class Solution(object):
    def missingNumber(self, nums):
        total=sum(nums)
        n=len(nums)
        expected=n*(n+1)//2
        return expected-total