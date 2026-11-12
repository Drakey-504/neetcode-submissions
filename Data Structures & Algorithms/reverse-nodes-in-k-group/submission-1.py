# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None

        dummy = ListNode(0, None)
        dummy_end = dummy

        l = r = head
        count = 1

        while r:

            if count%k == 0:
                r = r.next
                temp = l
                prev = None
                while count > 0:
                    nxt = temp.next
                    temp.next = prev
                    prev = temp
                    temp = nxt
                    count -= 1

                dummy_end.next = prev   
                dummy_end = l
                l=r
                count = 1 if r else 0 
            else:
                r = r.next
                count += 1    

        if count > 0:
            dummy_end.next = l

        return dummy.next            