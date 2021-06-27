
# implementation of queue using linked list-
# The queue, front stores the front node of LL and rear stores the last node of LL 

class linkedListNode:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        return

class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def EnQueue(self, item): 
        temp = linkedListNode(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.nextval = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.nextval
  
        if(self.front == None): 
            self.rear = None



q = Queue() 
q.EnQueue(10) 
q.EnQueue(20) 
q.DeQueue() 
q.DeQueue() 
q.EnQueue(30) 
q.EnQueue(40) 
q.EnQueue(50)  
q.DeQueue()    
print("Queue Front " + str(q.front.dataval))  # 40
print("Queue Rear " + str(q.rear.dataval))  # 50






