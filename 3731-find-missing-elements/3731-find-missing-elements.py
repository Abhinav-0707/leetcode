class Solution(object):
    def findMissingElements(self, nums):
        mini=min(nums)
        maxi=max(nums)
        s=set(nums)
        an=[]
        for i in range(mini,maxi+1):
            if i not in s:
                an.append(i)

        return an



        