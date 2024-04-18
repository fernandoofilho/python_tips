class Node:
    
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right = right 
        self.left = left
        
    def setRight(self, right):
        self.right = right
        
    def setLeft(self, left):
        self.left = left
        
    def setVal(self, val):
        self.val = val
        
        
    
def binTree(root: Node, n):
    #  1
    # 2 3
    return None