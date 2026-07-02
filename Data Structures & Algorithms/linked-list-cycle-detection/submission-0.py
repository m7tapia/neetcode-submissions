# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #simpler way is to store each node in a hashset and if we find a dupe then theres a cycle 

        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next

        return False


