class DLL:

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self,size):
        self.size = size
        self.cache = {}
        self.current_size = 0
        self.head = DLL(0,0)
        self.tail = DLL(0,0)
        self.head.next = self.tail
        self.tail.prev=self.head

    def deleteNode(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next


    def addToHead(self,node):

        node.next = self.head.next
        self.head.next.prev = node
        node.prev=self.head
        self.head.next=node


    def getValue(self,key):

        if key in self.cache:

            node = self.cache[key]
            self.deleteNode(node)
            self.addToHead(node)
            return self.cache[key].value

        return -1


    def setKeyValue(self,key,value):

        if key in self.cache:

            existing = self.cache[key]
            existing.value = value
            self.deleteNode(existing)
            self.addToHead(existing)

        else:
            new = DLL(key,value)
            self.cache[key] = new

            if self.size<=self.current_size:
                self.cache.pop(self.tail.prev.key)
                self.deleteNode(self.tail.prev)
                self.addToHead(new)
            else:
                self.current_size+=1
                self.addToHead(new)

        return True


if __name__=="__main__":

    cache = LRUCache(2)
    cache.setKeyValue(1,10)
    cache.setKeyValue(2,20)

    print(cache.getValue(1))

    cache.setKeyValue(19,21)

    print(cache.getValue(2))

    print("length" , len(cache.cache))
    print(cache.getValue(21))

    cache.setKeyValue(21,19)