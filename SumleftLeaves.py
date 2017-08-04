def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    res=0
    if not root:
        return 0

    if root.left and root.left.left==None and root.left.right==None:
        res+=root.left.val + self.sumOfLeftLeaves(root.right)
    else:
        res+=self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        # self.result.append(root.left.val)

    return res