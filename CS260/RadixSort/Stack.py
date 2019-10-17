class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def reverse(self):
         if len(self.items)>1:
            self.items.reverse()

     def size(self):
         return len(self.items)
