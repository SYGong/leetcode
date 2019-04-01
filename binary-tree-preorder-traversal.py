# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
 
    def preorderTraversal(self, root: TreeNode) -> List[int]:
                
        def preorderRecusion(node, out):
            if node is not None and node != 'null':
                out.append(node.val)
                preorderRecusion(node.left, out)
                preorderRecusion(node.right, out)
        
        result =[]
        preorderRecusion(root, result)
        return result

