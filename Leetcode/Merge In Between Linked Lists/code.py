# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        prev = None
        temp = ListNode(0)


        temp.next = list1
        count = 0
        
        while temp:
            
            if count == a:
                prev = temp 
                temp = temp.next
                break
                
            temp = temp.next
            count+=1
            
        prev.next = list2
        
        while prev.next:
            prev = prev.next
            
        while temp:
            
            if count == b:
                temp=temp.next
                break
                
            temp = temp.next
            count+=1
            
        prev.next = temp
        return list1
        