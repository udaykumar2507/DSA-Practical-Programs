class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class QueueByLL:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def isEmpty(self):
        return self.size==0
    def enqueue(self,data):
        new_node=Node(data)
        if (self.isEmpty()):
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
        self.size+=1
    def dequeue(self):
        if (self.isEmpty()):
            raise Exception("Queue is Empty")
        else:
            data=self.front.data
            self.front=self.front.next
            self.size-=1
            return data
    def  display(self):
        curr=self.front
        while(curr):
            print(curr.data)
            curr=curr.next
        
queue=QueueByLL()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print(queue.dequeue())
print()
queue.display()

