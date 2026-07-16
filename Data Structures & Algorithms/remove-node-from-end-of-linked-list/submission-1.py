# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # 1. Reverse the original list
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # `prev` is now the head of the reversed list
        reversed_head = prev

        # 2. Set up to traverse and find the Nth node
        curr = reversed_head
        prev = None # Keep prev as None initially to handle the n=1 edge case

        for _ in range(n - 1):
            prev = curr
            curr = curr.next

        # 3. Remove the target node
        if prev is None:
            # If n = 1, we are removing the first node of the reversed list
            reversed_head = curr.next
        else:
            # Standard case: wire the previous node to skip over 'curr'
            prev.next = curr.next

        # 4. Reverse the list back to its original order
        curr = reversed_head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 5. Return the restored list's new head
        return prev


    #Straight forward way to do it but maybe more work is to
    #first reverse the list than take off the node then reverse it back
    #Still O(n) time though



        
            

