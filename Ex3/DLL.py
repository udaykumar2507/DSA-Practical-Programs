class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None
class DLL:
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head is None
    def append(self,data):
        new_node=Node(data)
        if (self.head is None):
            self.head=new_node
            return
        curr=self.head
        while(curr.next is not None):
            curr=curr.next
        curr.next=new_node
        new_node.back=curr 
    # def append(self, data):
    #  new_node = Node(data)
    #  if self.head is None:
    #     self.head = new_node
    #  else:
    #     curr = self.head
    #     while curr.next is not None:
    #         curr = curr.next
    #     curr.next = new_node
    #     new_node.back = curr
    def prepend(self,data):
        new_node=Node(data)
        if (self.head is None):
            self.head=new_node
        curr=self.head
        curr.back=new_node
        new_node.next=curr
        self.head=new_node
    def remove(self,data):
        curr=self.head
        while(curr is not None):
            if (curr.data==data):
                if (curr.back is not None):
                    curr.back.next=curr.next
                else:
                    self.head=self.head.next
                if (curr.next is not None):
                    curr.next.back=curr.back
                return
            curr=curr.next
    def display(self):
        if self.is_empty():
            print("Doubly linked list is empty.")
            return

        curr=self.head
        while(curr is not None):
            print(curr.data)
            curr=curr.next
myDLl=DLL()
myDLl.append(3) 
myDLl.append(4)
myDLl.append(5)
myDLl.prepend(6)
print(myDLl.is_empty())
myDLl.display()   

           