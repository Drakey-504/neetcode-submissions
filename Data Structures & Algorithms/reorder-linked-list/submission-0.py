# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        one_step = head
        two_step = head

        while two_step and two_step.next:

            one_step = one_step.next
            two_step = two_step.next.next

        r = one_step.next

        one_step.next = None

        prev_node = None
        while r:
            next_node = r.next
            r.next = prev_node
            prev_node = r
            r = next_node

        l = head

        while l and prev_node:
            temp = l.next
            l.next = prev_node
            l = temp

            temp = prev_node.next
            prev_node.next = l
            prev_node = temp
        
        return None


        