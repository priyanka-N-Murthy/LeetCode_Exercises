class MinStack(object):

    def __init__(self):

        self.items=[]
        self.min_element=sys.maxint

    def push(self, x):

        self.items.append(x)
        if x < self.min_element:
            self.min_element = x

    def pop(self):

        if not self.items:
            return -1

        elementToPop = self.items[len(self.items)-1]

        if  (len(self.items) == 1):
            self.min_element=sys.maxint
            self.items=[]
            return
        elif (self.min_element==elementToPop) and (len(self.items) > 1):
            self.min_element = min( self.items[0:len(self.items)-1] )
            self.items = self.items[0:len(self.items)-1]
        else:
            self.items = self.items[0:len(self.items)-1]

    def top(self):

        if not self.items:
            return -1
        return self.items[len(self.items)-1]

    def getMin(self):
        
        if not self.items:
            return -1
        else:
            return self.min_element