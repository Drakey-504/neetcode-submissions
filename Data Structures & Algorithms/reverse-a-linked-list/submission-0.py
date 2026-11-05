# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next == None:
            return head


        prev_el = head
        head = head.next
        prev_el.next = None

        while head.next != None:
            nxt_el = head.next

            head.next = prev_el
            prev_el =  head
            head = nxt_el

        head.next = prev_el

        return head