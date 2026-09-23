class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        left = 0
        current = 0
        max_len = -1

        for right in range(len(nums)):
            current += nums[right]

            while current > target and left <= right:
                current -= nums[left]
                left += 1

            if current == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len