class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        mid = [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        return mid + left + right

