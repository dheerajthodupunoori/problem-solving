from heapq import heappop,heappush

class Node:

    def __init__(self,value):
        self.val = value
        self.next = None

    def __lt__(self,two):
        return self.val <= two.val


class MergeSortedLL:

    def __init__(self,lists):
        self.lists = lists
    
    def merge(self):

        heap = []

        for l in self.lists:

            heappush(heap,l)

        head ,temp = None , None

        while len(heap)>0:

            smallest = heappop(heap)
            print("Next smallest element --->", smallest.val)

            if temp is None:
                temp = smallest
                head = temp
            else:
                temp.next = smallest
                temp = temp.next

            if smallest.next:
                heappush(heap,smallest.next)

        return head


if __name__=="__main__":

     # total number of linked lists
    k = 3
 
    # a list to store the head nodes of the linked lists
    lists = [None] * k
 
    lists[0] = Node(1)
    lists[0].next = Node(4)
    lists[0].next.next = Node(7)
 
    lists[1] = Node(2)
    lists[1].next = Node(5)
    lists[1].next.next = Node(8)
    lists[1].next.next.next = Node(11)
 
    lists[2] = Node(3)
    lists[2].next = Node(6)
    lists[2].next.next = Node(9)

    merger = MergeSortedLL(lists)

    head = merger.merge()

    while head:

        print(head.val,head)
        head=head.next
 