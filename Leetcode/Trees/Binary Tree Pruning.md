https://leetcode.com/problems/binary-tree-pruning/submissions/


# *Binary Tree Pruning*

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed. A subtree of a node node is node plus every node that is a descendant of node.

#### Tags:

- Trees
- Depth-first-search
- Bread-first-search
- Tree-traversal

## Approach:

> So the question says that , we need to remove a subtree from the given tree if that subtree does not contain 1.
>
> The solution would be , simply checking for every sub-tree check if it contains "1" in it. If it does not have "1" in it then remove that subtree from the tree.
>
> To solve this problem , I have written a function "isOnePresent" which takes a node as input and returns "true" if that node as subtree contains "1" in it or else returns "false".
>
> Base condition is , if given root is null then directly return null as output.
>
> I have used queue to traverse through the tree nodes. Queue will contain a tuple which will have the (node,parent of node , direction).
>
> 1. node - node which we want to append to the queue
> 2. parent node - this is the parent of the node which we have appended - this parent node required because if there are no "1" present in subtree of "node" , then that subtree has to be removed from the tree.
> 3. direction - it tells if the node is left or right child of parent node.
>
> So , if we keep track of parent node and direction for each node , when ever sub-tree of that node does not contain "1" we can make of parent node and direction to remove that subtree from the given tree.
>
> Overall ,approach is traverse the tree from root. Insert root to queue with parent and direction as None. Repeat below steps until queue is not empty.
>
> 1. pop the element from the queue
> 2. check if the sub-tree of that node contains "1" in it 
>    1. if it contains 1 , then add left and right child of popped node to the queue
>    2. else , remove that sub-tree from the given tree

## Language:Python

```python
    from queue import deque

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def pruneTree(self, root: TreeNode) -> TreeNode:

            if root is None:
                return root
            queue = deque()
            queue.append((root,None,None))

            while len(queue) > 0:
                popped , parent , direction = queue.popleft()
                if self.isOnePresent(popped):
                    if popped.left:
                        queue.append((popped.left,popped,"left"))
                    if popped.right:
                        queue.append((popped.right,popped,"right"))
                else:
                    if parent == None:
                        return None
                    elif direction == "left":
                        parent.left = None
                    else:
                            parent.right = None
            return root

        def isOnePresent(self,node):
            if node.val == 1:
                return True
            if node.left and self.isOnePresent(node.left):
                return True
            if node.right and self.isOnePresent(node.right):
                return True
            return False
```