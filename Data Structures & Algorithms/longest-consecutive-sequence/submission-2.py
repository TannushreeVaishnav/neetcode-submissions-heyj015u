class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        lon=0
        for num in num_set:
            if num-1 not in num_set:
                curr=num
                leng=1
                while curr+1 in num_set:
                    curr+=1
                    leng+=1
                lon=max(leng,lon)
        return lon