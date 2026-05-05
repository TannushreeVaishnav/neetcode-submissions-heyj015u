class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        elem=0
        for i in nums:
            if cnt==0:
                cnt=1
                elem=i
            elif i==elem:
                cnt+=1
            else:
                cnt-=1
        return elem

        