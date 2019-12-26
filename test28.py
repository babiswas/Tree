class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None
       self.explored=False

   def reset(self):
       if self:
         if self.right:
            self.right.reset()
         self.explored=False
         if self.left:
            self.left.reset()

   def inorder(self):
       if self:
          if self.left:
             self.left.inorder()
          print(self.value)
          if self.right:
             self.right.inorder()

   def display_k(self,val,k):
       self.reset()
       stack=self.find_ancestor(val)
       stack1=[]
       for obj in stack:
          stack1.append(obj.value)
       stack1.pop()
       stack1=stack1[::-1]
       if k-1<len(stack1):
         print(stack1[k-1])

   def display(self,val):
       self.reset()
       stack=self.find_ancestor(val)
       stack1=[]
       for obj in stack:
          stack1.append(obj.value)
       print(stack1)
       

   def find_ancestor(self,val):
       stack=[]
       test=self
       while True:
          if test:
            stack.append(test)
            if test.value==val:
               return stack
            test=test.left
          elif stack:
            test=stack[-1]
            if not test.explored:
               test=test.right
               stack[-1].explored=True
            elif test.explored:
               stack.pop()
               test=None
          else:
              break
if __name__=="__main__":
   node=Node(12)
   node.left=Node(23)
   node.right=Node(25)
   node.left.left=Node(16)
   node.left.right=Node(11)
   node.right.left=Node(21)
   node.right.right=Node(28)
   node.display(25)
   node.display(16)
   node.display(21)
   node.display_k(21,2)



        