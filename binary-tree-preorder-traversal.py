class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        vals = []
        if root:
            vals.append(root.val)
            vals += self.preorderTraversal(root.left)
            vals += self.preorderTraversal(root.right)
        return vals