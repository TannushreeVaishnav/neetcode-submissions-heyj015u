class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for i in s:
            if i-1 not in s:
                cur=i+1
                while cur in s:
                    cur=cur+1
                lastel=cur-1
                ans=max(ans,lastel-i+1)
        return ans