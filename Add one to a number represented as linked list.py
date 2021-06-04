'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        
        borrow = self.add(head)
        
        if borrow > 0:
            
            temp = Node(borrow)
            temp.next = head
            head = temp
            
        return head
        
        
    def add(self,root):
        
        if root is None:
            return 1
            
        prev = root
        
        borrow = self.add(root.next)
        
        if borrow > 0:
            
            if prev.data == 9:
                
                prev.data = 0
                borrow = 1
                
            else:
                
                prev.data += 1
                borrow = 0
                
        return borrow