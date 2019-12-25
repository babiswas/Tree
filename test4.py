class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

  def preorder(self):
     if self:
        print(self.value)
        if self.left:
           self.left.preorder()
        if self.right:
           self.right.preorder()

  def inorder(self):
     if self:
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()

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
         print("Duplication Not allowed")

if __name__=="__main__":
   node=Node(12)
   node.insert(23)
   node.insert(25)
   node.insert(21)
   node.insert(24)
   node.insert(5)
   node.insert(1)
   node.insert(6)
   node.insert(10)
   print("Printing inorder traversal of the tree")
   node.inorder()
   print("Printing preorder traversal of the tree")
   node.preorder()


