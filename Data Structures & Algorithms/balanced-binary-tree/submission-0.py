# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # the isBalanced funtion is returning only one value but as balanced tree is check at every single node so we need hight for that and then calculate the balance but remember every step need to be balance in order to be the final tree balance
        
        def subBalance(root):
            if not root:
                return [True,0]  # As the an empty tree have left =0 and right =0 so 0-0 <=1 and is balanced and height is 0
            
            left, right = subBalance(root.left), subBalance(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1

            return [balanced, 1+max(left[1],right[1])]
        
        
        return subBalance(root)[0]

        