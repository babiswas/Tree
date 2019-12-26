import sys
class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None
      self.explored=False
  def display(self,stack):
     stack1=[]
     for i in stack:
        stack1.append(i.value)
     print(stack1)
         
  def find_path(self,v):
      stack=[]
      test=self
      while True:
         if test:
            stack.append(test)
            if test.value==v:
               self.display(stack)
               break
            test=test.left
         elif stack:
            test=stack[-1]
            if test.value==v:
              self.display(stack)
              break
            if test.explored:
               stack.pop()
               test=None
            elif not test.explored:
               stack[-1].explored=True
               test=test.right
         else:
            break
  def inorder(self):
     if self:
        if self.left:
           self.left.inorder()
        print(self.value)
        if self.right:
           self.right.inorder()

if __name__=="__main__":
   node=Node(12)
   node.left=Node(23)
   node.left.left=Node(25)
   node.left.right=Node(21)
   node.right=Node(52)
   node.right.left=Node(36)
   node.right.right=Node(47)
   node.right.right.left=Node(30)
   node.right.right.right=Node(43)
   print("Inorder traversal of the node")
   node.inorder()
   print("The distance form root to given node")
   node.find_path(int(sys.argv[1]))

   

  
            