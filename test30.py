class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def inorder(self):
       if self:
          if self.left:
             self.left.inorder()
          print(self.value)
          if self.right:
             self.right.inorder()

   def isMirror(self,node):
      if self==None and node==None:
           return True
      elif self==None or node==None:
           return False
      else:
          return self.value==node.value and isMirror(self.left,node.right) and isMirror(self.right,node.left)


if __name__=="__main__":
  node1=Node(12)
  node1.left=Node(23)
  node1.right=Node(25)
  node1.left.left=Node(16)
  node1.left.left.left=Node(1)
  node1.left.left.right=Node(2)
  node1.left.right=Node(17)
  node1.right.left=Node(5)
  node1.right.left.left=Node(11)
  node1.right.left.right=Node(8)
  node1.inorder()


           