class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

   def inorder(self):
      stack=[]
      test=self
      while True:
         if test:
            stack.append(test)
            test=test.left
         elif stack:
            test=stack.pop()
            print(test.value)
            test=test.right
         else:
            break
          
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
   node.insert(18)
   node.insert(16)
   node.insert(17)
   node.insert(7)
   node.insert(9)
   node.insert(3)
   node.insert(2)
   node.inorder()

