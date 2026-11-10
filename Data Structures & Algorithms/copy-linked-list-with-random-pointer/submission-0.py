"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        rand_indexes = {}

        temp = head
        ind = 0
        while temp:
            rand_indexes[temp] = [ind, temp.val, None]
            ind += 1
            temp = temp.next
        
        temp = head
        ind = 0
        while temp:
            if temp.random:
                rand_indexes[temp][2] = rand_indexes[temp.random][0]
            temp = temp.next
            ind += 1
             
        dummy = Node(0)
        temp = dummy

        new_hash = {}
        for n in rand_indexes.values():
            temp.next = Node(n[1], None, None)
            new_hash[n[0]] = temp.next
            temp = temp.next
        temp = dummy.next

        for n in rand_indexes.values():
            if n[2] is not None:
                temp.random = new_hash[n[2]]
            temp = temp.next

        return dummy.next        