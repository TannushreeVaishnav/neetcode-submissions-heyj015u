class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        low,high,mid=0,n-1,0
        while(mid<=high):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        
        