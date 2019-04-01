class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        stack = []
        cur = root
        
        while cur or len(stack) > 0:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                cur = node.right
        return res