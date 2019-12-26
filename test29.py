class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def display(stack):
     stack1=[]
     for obj in stack:
         stack1.append(obj.value)
     print(stack1)

def find_path_leaf(node,stack):
    if node:
       if node.left:
          find_path_leaf(node.left,stack)
       stack.append(node)
       if node.right==None and node.left==None:
          display(stack)
       if node.right:
          find_path_leaf(node.right,stack)
    stack.pop()

if __name__=="__main__":
   stack=[]
   node=Node(12)
   node.left=Node(23)
   node.right=Node(25)
   node.left.left=Node(16)
   node.left.right=Node(18)
   node.right.left=Node(29)
   node.right.right=Node(46)
   find_path_leaf(node,stack)

           
      