class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

   def height(self):
       count=0
       queue=[]
       queue.append(self)
       while queue:
           q_len=len(queue)
           count=count+1
           while q_len:
               m=queue.pop(0)
               if m.left:
                  queue.append(m.left)
               if m.right:
                  queue.append(m.right)
               q_len=q_len-1
       return count

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
   node.insert(19)
   node.insert(16)
   node.insert(5)
   node.insert(1)
   node.insert(6)
   node.insert(10)
   print(node.height())
