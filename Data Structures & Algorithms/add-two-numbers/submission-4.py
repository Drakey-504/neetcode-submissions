# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        t1 = l1
        t2 = l2

        dummy_head = ListNode(0, None)
        res = dummy_head
        carry = 0

        while t1 or t2:

            val1 = 0
            val2 = 0

            if t1:
                val1 = t1.val
                t1 = t1.next             
            if t2:
                val2 = t2.val
                t2 = t2.next

            resval = val1 + val2 + carry
            carry = 0

            if resval > 9:
                resval = resval%10
                carry = 1

            res.next = ListNode(resval, None)
            res = res.next

        if carry:
            res.next = ListNode(1,None)

        return dummy_head.next            


