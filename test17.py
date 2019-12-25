class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def mirror(node):
   if not node:
      return node
   else:
      left=node.left
      right=node.right
      node.left=right
      node.right=left
      mirror(node.left)
      mirror(node.right)
      return node

def level_trav(node):
     queue=[]
     queue.append(node)
     while queue:
         m=queue.pop(0)
         print(m.value)
         if m.left:
           queue.append(m.left)
         if m.right:
           queue.append(m.right)

if __name__=="__main__":
   node=Node(12)
   node.left=Node(21)
   node.right=Node(41)
   node.left.left=Node(23)
   node.left.right=Node(28)
   node.right.left=Node(45)
   node.right.right=Node(47)
   print("The level order traversal of the tree")
   level_trav(node)
   node=mirror(node)
   print("The level order traversal of the tree after mirroring")
   level_trav(node)
   
