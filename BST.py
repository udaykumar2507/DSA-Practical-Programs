class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if (self.key<data):
            if (self.lchild):
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if (self.rchild):
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
         if self.key==data:
             print("Element Found")
             return
         if (self.key<data):
            if (self.lchild):
                self.lchild.search(data)
            else:
                print("Element Not Found")
         else:
            if (self.rchild):
                self.rchild.search(data)
            else:
                print("Element Not Found")
    def preorder(self):
        print(self.key)
        if (self.lchild):
            self.lchild.preorder();
        if (self.rchild):
            self.rchild.preorder();
root=BST(10)
root.insert(100)
root.insert(1000)
root.insert(10000)
root.insert(12)
root.preorder()
root.search()






                
        
            
