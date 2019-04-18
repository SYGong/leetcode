class Solution:
    def searchBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        
        
        
        
        # public solution 1 ... 
        # iteration
        while root != None and val != root.val:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
        return root