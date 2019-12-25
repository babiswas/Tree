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

  def print_common(self,node2):
      stack1=[]
      stack2=[]
      test1=self
      test2=node2
      while True:
          if test1:
             stack1.append(test1)
             test1=test1.left
          elif test2:
             stack2.append(test2)
             test2=test2.left
          elif stack1 and stack2:
             test1=stack1[-1]
             test2=stack2[-1]
             if test1.value==test2.value:
                print(test1.value)
                stack1.pop()
                stack2.pop()
                test1=test1.right
                test2=test2.right
             elif test1.value>test2.value:
                stack2.pop()
                test2=test2.right
                test1=None
             else:
                stack1.pop()
                test1=test1.right
                test2=None
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
        print("duplication not allowed")

if __name__=="__main__":
   node=Node(12)
   print("Constructing Tree1")
   node.insert(21)
   node.insert(18)
   node.insert(16)
   node.insert(20)
   node.insert(19)
   node.insert(5)
   node.insert(7)
   node.insert(10)
   node.insert(1)
   node.insert(0)
   node.insert(3)
   node.insert(11)
   print("Inorder of tree1")
   node.inorder()
   print("Consrtucting Tree2")
   node1=Node(14)
   node1.insert(18)
   node1.insert(20)
   node1.insert(12)
   node1.insert(11)
   node1.insert(8)
   node1.insert(13)
   node1.insert(22)
   print("Inorder of the tree2")
   node1.inorder()
   print("Printing the common nodes of the tree")
   node.print_common(node1)
   
