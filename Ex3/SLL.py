class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def isempty(self):
        return self.head is None
    def append(self,data):
        new_node=Node(data)
        if (self.head is None):
            self.head=new_node
            return
        current=self.head
        while(current.next is not None):
            current=current.next
        current.next=new_node
    def prepend(self,data):
        new_Node=Node(data)
        if (self.head is None):
            self.head=new_Node
            return
        new_Node.next=self.head
        self.head=new_Node
    def remove(self,data):
        if (self.head.data==data):
          self.head=self.head.next
          return
        curr=self.head
        while(curr.next is not None):
            if (curr.next.data==data):
                curr.next=curr.next.next
                return
            curr=curr.next
    def  display(self):
        curr=self.head
        while(curr is not None):
            print(curr.data,end="=>")
            curr=curr.next
MyLL=SLL()
MyLL.append(5)
MyLL.append(10)
MyLL.append(7)
MyLL.prepend(99)
MyLL.remove(99)
print(MyLL.isempty())
MyLL.display()        


    

