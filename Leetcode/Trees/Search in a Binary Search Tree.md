https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the `root` of a binary search tree (BST) and an integer `val`. Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

##### Tags:

- Tree
- Binary Search Tree
- Tree Traversal

##### Difficulty Level: Easy

##### Approach:

> Since the given tree is binary search tree , in binary search tree root is always greater than left child and less than the right child.
>
> So , traverse a tree from root and follow below steps:
>
> 1. while root is not empty
>    1. if root is equal to given value - return root
>    2. if root is greater than value , traverse to the left of the tree 
>    3. if root is less than the given value , traverse to the right of the tree
> 2. if there is no node present in the tree which is equal to the given value , at the end return null

#### Language:Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None
     
```