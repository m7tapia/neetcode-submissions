# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
   

   
        #A simpler but harder-to-come-by approach is to have two pointers. One is going to start at the first node, 
        #and then the next is going to start exactly N nodes ahead of it. When the ahead node hits null, our behind node is going to be 
        #exactly where we want it to be because the space between them is exactly N.

        #But the thing is, we're at the node that we want to replace, when we actually need to 
        #be at the previous node. So, an easy way to fix that is to create a dummy node in the beginning and have our behind node 
        #start at that dummy node instead of the first node. Then, we land exactly at the previous node that we want to delete.
        
        if not head:
            return None

        if not head.next:
            return None

        dummy = ListNode()
        dummy.next = head

        behind = dummy
        curr = head
        for _ in range(n):
            curr = curr.next
        ahead = curr

        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next

        return dummy.next

            


