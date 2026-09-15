# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter =[0]
        self.height(root,maxdiameter)
        return maxdiameter[0]

    def height(self,root,maxdiameter):
        if root is None:
            return 0

        lheight = self.height(root.left,maxdiameter)
        rheight = self.height(root.right,maxdiameter)

        maxdiameter[0] = max(maxdiameter[0], lheight + rheight) 

        return 1 + max(lheight,rheight)