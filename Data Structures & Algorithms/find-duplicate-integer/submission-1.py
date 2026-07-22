class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Find the intersection point
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find the entrance to the cycle
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow