class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

def is_present(node,val1):
   if not node:
      return False
   else:
      if node.value==val1:
         return True
      else:
        return is_present(node.left,val1) or is_present(node.right,val1)

def lca(node,val1,val2):
   if not node:
      return None
   else:
       if is_present(node,val1) and is_present(node,val2):
          if node.value==val1 or node.value==val2:
               return node
          else:
             left=lca(node.left,val1,val2)
             right=lca(node.right,val1,val2)
             if right:
                return right
             if left:
                return left
             return node
       else:
         return None

if __name__=="__main__":
   node=Node(12)
   node.left=Node(23)
   node.right=Node(17)
   node.left.left=Node(24)
   node.left.right=Node(29)
   node.right.left=Node(16)
   node.right.right=Node(11)
   node.right.right.left=Node(34)
   node.right.right.right=Node(13)
   m=lca(node,17,11)
   if m:
     print(m.value)
   else:
     print("No ancestor found")




   
   
