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

   def min(self,node):
      test=node
      while test.left:
         test=test.left
      return test
      
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

   def inorder_sucessor(self,node,node1):
       if node1.right:
         return self.min(node1.right)
       else:
         test=node
         prev=None
         while test:
            if test.value>node1.value:
               prev=test
               test=test.right
            elif test.value<node1.value:
               test=test.right
            else:
               return prev
         return test
       

   def search(self,value):
      if not self:
         return None
      else:
         test=self
         while test:
            if test.value>value:
               test=test.left
            elif test.value<value:
               test=test.right
            else:
               return test
         return test

if __name__=="__main__":
   node=Node(12)
   node.insert(23)
   node.insert(25)
   node.insert(21)
   node.insert(17)
   node.insert(10)
   node.insert(20)
   node.insert(5)
   node.insert(7)
   node.insert(11)
   node.insert(2)
   node.insert(3)
   node1=node.search(17)
   print("The inorder traversal of the tree")
   node.inorder()
   print("Printing the inorder sucessor of BST")
   print(node.inorder_sucessor(node,node1).value)