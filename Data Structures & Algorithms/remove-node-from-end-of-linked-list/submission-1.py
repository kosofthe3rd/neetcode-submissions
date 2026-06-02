# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        point = head
        while point:
            point = point.next
            count += 1
        
        k = count - n 
        if k == 0:
            return head.next
            
        t = head
        while k > 1:
            t = t.next
            k -= 1

        t.next = t.next.next
        return head


        