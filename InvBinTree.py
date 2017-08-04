def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if (root==None):
        return None
    if root:
        right=root.right
        left=root.left
        root.right=self.invertTree(left)
        root.left=self.invertTree(right)
    return root