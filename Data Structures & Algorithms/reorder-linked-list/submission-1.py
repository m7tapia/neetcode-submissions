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
        #pass by ref
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        #now each index holds a node. remember that these indices are still the same nodes in memory
        #and still have their pointers
            
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
            
        # Step 3: The now last node will still hold the pointer it had in in the original list
        #so we update its pointer to None to get out of that infinite loop.
        nodes[i].next = None

        #we don't have to return anything since we just moved the input list in place


        #This solution is O(n) time and O(n) space