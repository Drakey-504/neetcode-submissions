class DNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prevp = None
        self.nextp = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = DNode(0,0), DNode(0,0)
        self.left.nextp = self.right
        self.right.prevp = self.left
        self.lookup = {}
        self.cap = capacity

    def remove(self, node):
        prev, nxt = node.prevp, node.nextp
        prev.nextp = nxt
        nxt.prevp = prev


    def insert(self, node):
        prev, nxt = self.right.prevp, self.right
        prev.nextp = nxt.prevp = node
        node.prevp = prev
        node.nextp = nxt


    def get(self, key: int) -> int:

        if key in self.lookup: 
            self.remove(self.lookup[key])
            self.insert(self.lookup[key])
            return self.lookup[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:

        newNode = DNode(key, value)

        if key in self.lookup:
            self.remove(self.lookup[key])

        self.insert(newNode)
        self.lookup[key] = newNode    

        if len(self.lookup) > self.cap:
            self.lookup.pop(self.left.nextp.key)
            self.remove(self.left.nextp)
        
