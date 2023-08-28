class Node:
    def __init__(self,val:int=0,next:'Node'=None):
        self.val=val
        self.next=next
    def __str__(self) -> str:
        return f'[{self.val},next:{self.next}]'
class MyStack:
    def __init__(self):
        self.head=None
    def push(self, x: int) -> None:
        if(self.empty()):
            self.head=Node(x)
        else:
            newNode=Node(x,self.head)
            self.head=newNode
    def pop(self) -> int:
        val=self.head.val
        self.head=self.head.next
        return val
    def top(self) -> int:
        return self.head.val
    def empty(self) -> bool:
        if self.head == None:
            return True
        else:
            return False
        
# Your MyStack object will be instantiated and called as such:
x=1
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.top()
print(param_2,param_3,obj.empty())
print(obj.head)
# param_4 = obj.empty()