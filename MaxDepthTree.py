def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root==None:
        return 0

    l=self.maxDepth(root.left)
    r=self.maxDepth(root.right)

    if l>r:
        l+=1
        return l
    else:
        r+=1
        return r