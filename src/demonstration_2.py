"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        # Your code here
        self.input_stack = Stack()
        self.output_stack = Stack()
        
    def enqueue(self, item):
        # Your code here
        self.input_stack.push(item)

    def dequeue(self):
        # we are going to return the values from the output stack
        # if the output stack is empty, fill it with values from the input stack
        if len(self.output_stack.data) == 0:
            while len(self.input_stack.data) > 0:
                # pop from the input_stack and push onto the output_stack
                current_item = self.input_stack.pop()
                self.output_stack.push(current_item)
                
        return self.output_stack.pop()  
    
    
my_queue = QueueTwoStacks()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
print(f"The first item added was {my_queue.dequeue()}")
print(f"The second item added was {my_queue.dequeue()}")
my_queue.enqueue("E")
print(f"The third item added was {my_queue.dequeue()}")
print(f"The fourth item added was {my_queue.dequeue()}")
print(f"The fifth item added was {my_queue.dequeue()}")       
                
                
        

