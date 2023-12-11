class LISTADT:
    def __init__(self,capacity=10):
        self.capacity=capacity
        self.size=0
        self.array=[None]*self.capacity
    def isempty(self):
        return self.size==0
    def length(self):
        return self.size
    def append(self,value):
        if (self.size==self.capacity):
            self.resize()
        self.array[self.size]=value
        self.size+=1
    def resize(self):
        new_capacity=self.capacity*2
        new_array=[None]*new_capacity
        for i in range(self.size):
            new_array[i]=self.array[i]
        self.array=new_array
        self.capacity=new_capacity
    def get(self,index):
        if (0<=index<self.size):
            return self.array[index]
        else:
            print("Index Out Of Bound")
    def set(self,index,value):
        if (0<=index<self.size):
            self.array[index]=value
        else:
            print("Index Out of Bound")
    def remove(self,value):
        if (self.indexof!=-1):
            index=self.indexof(value)
            self.remove_at(index)
        else:
            print("Element Not Found")
    def indexof(self,value):
        for i in range(self.size):
            if (self.array[i]==value):
                return i
        return -1
    def remove_at(self,index):
        if 0<=index<self.size:
            for i in range(index,self.size-1):
                self.array[i]=self.array[i+1]
            self.array[self.size-1]=None
            self.size-=1
    def display(self):
        result="["
        for i in range(self.size):
            result+=str(self.array[i])
            if (i<self.size-1):
                result+=","
        result+="]"
        return result
myList=LISTADT()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
print(myList.get(3))
myList.set(1,45)
myList.remove(4)
print(myList.display())
print(myList.length())
print(myList.isempty())



        
            


        
