#Idealy when implementing  a linked list , we define a node and a linked list iusing different classes

#We therefore create our stack's node
#It contains data stored in the stacknode and a pointer the next node
class stackNode:
    #constructor to initialize a node
    def __init__(self,data):
        self.data = data
        self.next = None

#Class containing our stack(linkedlist)
class stackLinked:
    #Constructor to initialize the beginning of a linked list
    def __init__(self):
        self.head = None
    #Check if empty 
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    #Push into the stack        
    def push(self,data):
        newNode = stackNode(data)
        newNode.next = self.head
        self.head = newNode
        print(newNode.data) 

    #Pop out of the stack
    def pop(self):
        if self.head is None:
            print("Stack underflow")
        else:
            delete = self.head.data
            self.head = self.head.next
            return delete       
    
    #Top element in the stack
    def top(self):
        return self.head.data
Stack = stackLinked()
Stack.push(10)
Stack.push(20)
Stack.push(30)
Stack.push(40)
Stack.push(50)  

print ("% d popped from stack" % (Stack.pop()))
print ("Top element is % d " % (Stack.top()))


        


      
              