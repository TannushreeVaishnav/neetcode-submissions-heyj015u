class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        maxi=-(2**31)
        for i in nums:
            cursum+=i
            maxi=max(maxi,cursum)
            if cursum<0:
                cursum=0
        return maxi
        