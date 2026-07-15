# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Step 1: Store all nodes in an array
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
            
        # Step 2: Use two pointers at each end of the array
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            
            # Break early if we've reached the middle
            if i >= j:
                break
                
            nodes[j].next = nodes[i]
            j -= 1
            
        # Step 3: Terminate the final node to avoid cycles
        nodes[i].next = None