# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #start out with a dummy node to not worry about 
        #the edge case of inserting into an empty list
        dummy = ListNode()
        tail = dummy
        

        while list1 and list2:
            if list1.val > list2.val:
                #add the lesser and then move that one forward
                tail.next = list2
                list2 = list2.next

            else:
                #add the lesser and then move that one forward
                tail.next = list1
                list1 = list1.next
            #move th tail forward b/ we added a new node
            tail = tail.next

        #finish out with whichever still had nodes
        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next

        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next

        #return the head
        return dummy.next

    #O(n+m) time and O(1) space