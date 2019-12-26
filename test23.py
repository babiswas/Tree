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

def is_Mirror(node1,node2):
    if node1==None and node2==None:
         return True
    elif node1==None or node2==None:
         return False
    elif node1.value!=node2.value:
         return False
    else:
        return node1.value==node2.value and is_Mirror(node1.left,node2.right) and is_Mirror(node1.right,node2.left)

if __name__=="__main__":
  print("Constructing tree1")
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
  node1.left.left.right.left=Node(90)
  print("Constructing Tree 2")
  node2=Node(12)
  node2.left=Node(25)
  node2.right=Node(23)
  node2.right.right=Node(16)
  node2.right.left=Node(17)
  node2.right.right.right=Node(1)
  node2.right.right.left=Node(2)
  node2.left.right=Node(5)
  node2.left.right.right=Node(11)
  node2.left.right.left=Node(8)
  print("Inorder traversal")
  node1.inorder()
  print("Inorder traversal")
  node2.inorder()
  print("Comparing the trees")
  print(is_Mirror(node1,node2))





           