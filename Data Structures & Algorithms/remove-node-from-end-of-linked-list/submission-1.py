# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return None
                  
        end = head       
        count = 0

        while count < n:
            end = end.next
            count += 1

        prev_node = None
        n_from_end = head

        while end:
            prev_node = n_from_end
            n_from_end = n_from_end.next
            end = end.next

        if prev_node is None:
            head = head.next
        elif n_from_end.next:
            prev_node.next = n_from_end.next
        else:
            prev_node.next = None

        return head                


        