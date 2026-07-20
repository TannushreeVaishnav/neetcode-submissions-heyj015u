# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        merged=lists[0]
        for i in range (1,len(lists)):
            merged=self.mergeTwoLists(merged,lists[i])
        return merged
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        p1=list1
        p2=list2
        while p1 and p2:
            if p1.val<=p2.val:
                curr.next=p1
                p1=p1.next
            else:
                curr.next=p2
                p2=p2.next
            curr=curr.next
        if p1:
            curr.next=p1
        if p2:
            curr.next=p2
        return dummy.next
        
        