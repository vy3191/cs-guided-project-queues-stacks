class LinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  
class Queue:
  def __init__(self):
    self.front = None
    self.end = None
  
  def enqueue(self, item):
    # create a new node
    new_node = LinkedListNode(item)
    if self.end is None:
      self.end = new_node
      self.front = new_node
    else:
      self.end.next = new_node
      self.end = new_node  
  def dequeue(self):
    if self.front is None:
      return None
    # store the front to the temp
    temp = self.front
    # move the front to the nex node over
    self.front = self.front.next
    temp.next = None
    
    # special case if the queue should now be empty
    if self.front is None:
      self.end = None
    
    return temp.data   
      
      
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
      
    
    