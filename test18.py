class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def inorder(node):
   if node:
      if node.left:
         inorder(node.left)
      print(node.value)
      if node.right:
         inorder(node.right)


def delete_full_tree(node):
   if node:
     node=delete_tree(node)
     node=None
     return node
      
      

def delete_tree(node):
  if not node:
      return 
  else:
     delete_tree(node.left)
     delete_tree(node.right)
     print(f"deleting{node.value}")
     node.left=None
     node.right=None
     del node
     node=None

if __name__=="__main__":
   node=Node(12)
   node.left=Node(21)
   node.right=Node(22)
   node.left.left=Node(25)
   node.left.right=Node(27)
   node.right.left=Node(16)
   node.right.right=Node(19)
   inorder(node)
   node=delete_tree(node)
   inorder(node)

   
