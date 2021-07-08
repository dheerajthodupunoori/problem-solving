# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        length = len(lists)
        
        if length == 0:
            return None
        
        
        head = lists[0]
        
        for i in range(1,length):
            
            temp = head
            
            head = self.merge2Lists(temp,lists[i])
        
        return head
        
        
        
    def merge2Lists(self,list1,list2):
        
        head = dummy = ListNode(0)
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                
                dummy.next = list1
                list1 = list1.next
                
            else:
                
                dummy.next = list2
                list2=list2.next
                
            dummy = dummy.next
            
        if list1:
            dummy.next = list1
        
        if list2:
            dummy.next = list2
                
        return head.next
        