class Solution(object):
    def isPalindrome(self, s):
        result=""
        for ch in s:
            if ch.isalnum():
                result+=ch.lower()
        reverse=result[::-1]
        return reverse==result