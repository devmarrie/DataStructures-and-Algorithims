# Defining the class containing the node
class l_node:
    def __init__(self,data):
         self.data = data
         self.pointer = None

#class containg our queue
class l_queue:
    def __init__(self):
        self.head = None
    
    #Check if empty
    def isEmpty(self):
        if self.head == None:
            print("The  queue is empty")

    #Enqueue
    def enqueue(self,item):
        newNode = l_node(item)
        self.head = newNode
        newNode.pointer = self.head

    #Front value in the queue
    def front(self):
        print(self.head.data)

    #Rear
    def rear(self):
        print(self.head.data[0])
    
    #Front
    def front(self):
        print(self.head.data)

    #dequeue
    def dequeue(self):
        remove = self.head.data
        self.head = self.head.pointer
        return remove

lq = l_queue()
lq.isEmpty()
lq.enqueue(6)
lq.enqueue(12)
lq.enqueue(24)
lq.enqueue(36)
print(lq.head.data)
lq.dequeue()

