# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



#we reverse the second part of the list so we can easily link them in the way we want
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Edge case
        if not head:
            return

        #first we need to know where the middle of the list is so we use a slow and fast pointer
        #where the slow pointer ends will be the middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next

        #we start to reverse the second part of the list
        slow.next = prev = None
    
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #Now we rewire and making sure to save our nexts
        while prev: #prev is the head of our reversed second part now
            temp1, temp2 = head.next, prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2
            
        #O(n) time and O(1) space






        

