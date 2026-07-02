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

        #This is O(n) time b/c if we start both pointers next to each other. The distance between them will be n - 1.
        #It'll take us n -1 iterations for them to meet. For example, say the distance is 10.
        #small pointer moves once, fast pointer moves twice, 10 + (1 - 2) = 9. It'll take 10 iterations
        #to close the gap. That's why it'll be in O(n) time.

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False