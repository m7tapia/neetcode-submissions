# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #better way is to use the fast and slow pointer (tortoise and the hare algo)

        #one pointer moves forward two at a time (if there's no cycle obviously this one will reach null first)
        #other pointer moves forward once at a time
        #if there's a cycle they're bound to meet each other again

        #This is O(n) time b/c if we start both pointers next to each other. Imagine a circle where we start
        #both at the same spot. Distance between them is n = 10. Slow moves forward one and fast moves forward two.
        #The new distance between them will be 9. It'll take 10 iterations for them to meet again. That's why the 
        #time complexity is O(n)

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

        #O(n) time and O(n) space