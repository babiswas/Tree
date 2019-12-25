class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

   def rev_level(self):
      stack=[]
      queue=[]
      queue.append(self)
      while queue:
         m=queue.pop(0)
         stack.append(m)
         if m.right:
           queue.append(m.right)
         if m.left:
           queue.append(m.left)
      while stack:
         print(stack.pop().value)

   def insert(self,value):
      if self.value>value:
         if self.left:
            self.left.insert(value)
         else:
            self.left=Node(value)
      elif self.value<value:
         if self.right:
            self.right.insert(value)
         else:
            self.right=Node(value)
      else:
         print("Duplication not allowed")

if __name__=="__main__":
  node=Node(12)
  node.insert(22)
  node.insert(16)
  node.insert(18)
  node.insert(14)
  node.insert(15)
  node.insert(24)
  node.insert(23)
  node.insert(5)
  node.insert(7)
  node.insert(1)
  node.insert(0)
  node.rev_level()

