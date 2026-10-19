# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # remember when there is tree or linked list they have in built variables which helps likein linkedlist list.next, head etc and in tree we have .left .right, root etc.

        if not root:
            return None
        
        root.right, root.left = root.left, root.right
    
        self.invertTree(root.right)
        self.invertTree(root.left)
        

        return root
