from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        pairs=count.most_common(k)
        res=[]
        for num,freq in pairs:
            res.append(num)
        return res

        
        
        