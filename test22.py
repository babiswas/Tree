import sys
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

def find_path_leaf(node,stack,v):
    if not node:
       return
    stack.append(node)
    find_path_leaf(node.left,stack,v)
    if node.value==v:
       display(stack)
    find_path_leaf(node.right,stack,v)
    stack.pop()

if __name__=="__main__":
   stack=[]
   node=Node(12)
   node.left=Node(10)
   node.left.left=Node(23)
   node.left.right=Node(25)
   node.left.left.left=Node(20)
   node.left.left.right=Node(22)
   node.right=Node(30)
   node.right.left=Node(5)
   node.right.right=Node(1)
   node.right.right.left=Node(9)
   node.right.right.right=Node(13)
   find_path_leaf(node,stack,int(sys.argv[1]))

           
      