class Node:
   def __init__(self,value):
     self.value=value
     self.left=None
     self.right=None


def lca(node,val1,val2):
    left=None 
    right=None
    if not node:
       return None
    else:
       if is_present(node,val1) and is_present(node,val2):
          if node.value==val1 or node.value==val2:
                return node
          else:
             left=lca(node.left,val1,val2)
             right=lca(node.right,val1,val2)
             if left:
                return left
             elif right:
                return right
             else:
                return node
       else:
         return None
             

def is_present(node,val):
    if not node:
       return False
    else:
       if node.value==val:
          return True
       return is_present(node.left,val) or is_present(node.right,val)

if __name__=="__main__":
   node=Node(12)
   node.left=Node(1)
   node.right=Node(3)
   node.left.left=Node(30)
   node.left.right=Node(14)
   node.right.left=Node(16)
   node.right.right=Node(7)
   node.left.left.left=Node(20)
   print(is_present(node,12))
   print(is_present(node,14))
   print(is_present(node,29))
   m=lca(node,7,14)
   if m:
     print(m.value)
   else:
     print("No lca for the given pairs")

