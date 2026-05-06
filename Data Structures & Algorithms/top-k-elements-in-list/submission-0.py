class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Sort numbers by frequency (highest first)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Take the first k numbers
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result

        