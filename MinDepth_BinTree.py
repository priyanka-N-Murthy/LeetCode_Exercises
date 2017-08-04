class Solutions():
    def minDepth(self, root):

        left=None
        Right=None
        head=root

        if head==None:
            return 0
        elif head.left==None:
            return self.minDepth(head.right)+1
        elif head.right==None:
            return self.minDepth(head.left)+1
        else:
            return min(self.minDepth(head.right),self.minDepth(head.left))+1
