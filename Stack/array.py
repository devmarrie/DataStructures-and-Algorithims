# maxsize return infinite when stack is empty
from sys import maxsize

# Create a stack


def arrStack():
    stack = []
    return stack
# defining when a stac is empty


def isEmpty(stack):
    return len(stack) == 0

# Function to push into the stack


def push(stack, item):
    stack.append(item)

# Popping out an item from  stack


def pop(stack):
    stack.pop()

# Returning the top element


def top(stack):
    return stack[len(stack) - 1]


# Now lets test our functions
ourStack = arrStack()
push(ourStack, 10)
push(ourStack, 20)
push(ourStack, 30)
push(ourStack, 40)
push(ourStack, 50)
# Now lets veiw our stack
print(ourStack)

# pop
pop(ourStack)
print(f'Our stack after poping,{ourStack}')

# view the top element
top(ourStack)
print(f'Our top element,{ourStack}')
