def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    tmp=[]
    def dfs(root):
        if not root :
            return []
        if root:
            tmp.append(root.val)
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    return tmp