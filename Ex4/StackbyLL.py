class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class StackByLL:
    def __init__(self):
        self.top=None
        self.size=0
    def isempty(self):
        return self.size==0
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
        self.size+=1
    def pop(self):
        if (self.size==0):
            raise Exception("stack is Empty")
        data=self.top.data
        self.top=self.top.next
        self.size-=1
        return data
    def peek(self):
        if (self.size==0):
            raise Exception("Stack is Empty")
        data=self.top.data
        return data
    def display(self):
        curr=self.top
        while(curr):
            print(curr.data)
            curr=curr.next
stack=StackByLL()
stack.push(1)
stack.push(2)
stack.push(3)
print("print without deleying",stack.peek())
print(stack.display())
print("printing after Del",stack.pop())
stack.display()
