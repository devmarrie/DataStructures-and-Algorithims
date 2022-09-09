#Usin a class to create a queue 
class queue:
    def __init__ (self):
        self.items = []

    #Check if the queue is empty
    def isEmpty(self):
        if len(self.items) == 0:
            print("Queue is empty")
        else:
            print ("Queue is not empty")
    #Check if the queue is full
    #def isFull(max,self):
       # if self.items == max:
           # print("Queue is Full")
        #else:
           # print("Queue is not yet full")

    #Front
    def front(self):
        print(f'The top most value of the queue is {self.items[0]}')
    
    #Rear
    def rear(self):
        print(f'The value at the rear end of the queue is {self.items[-1]}')
    
    #Enqueue
    def enqueue(self,data):
        self.items.append(data)

    #Dequeue
    def dequeue(self):
        self.items.pop(0)
        print(self.items)

#Function calls
q = queue()
q.isEmpty()
q.enqueue(20)
q.enqueue(40)
q.enqueue(60)
q.enqueue(80)
q.enqueue(90)
print(q.items)
q.front()
q.rear()
q.dequeue()


