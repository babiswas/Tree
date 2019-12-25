class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def lvl_order(self):
       queue=[]
       queue.append(self)
       while queue:
          m=queue.pop(0)
          print(m.value)
          if m.left:
            queue.append(m.left)
          if m.right:
            queue.append(m.right)

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
   node.insert(23)
   node.insert(25)
   node.insert(21)
   node.insert(16)
   node.insert(15)
   node.insert(17)
   node.insert(5)
   node.insert(1)
   node.insert(10)
   node.insert(11)
   node.lvl_order()


