# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        def mergeTwoLists(l1, l2):
            
            dummy_head = temp = ListNode(0)

            while l1 and l2:
                if l1.val <= l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next

                temp = temp.next        

            if l1:
                temp.next = l1

            if l2:
                temp.next = l2

            return dummy_head.next
        
        
        while len(lists) > 1:
            new_list = []
            i = 0
            while i < len(lists):
                if i+1 < len(lists):
                    new_list.append(mergeTwoLists(lists[i], lists[i+1]))
                    i += 1
                else:
                    new_list.append(lists[i])
                i += 1        

            lists = new_list        

        return lists[0]    




