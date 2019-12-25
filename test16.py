class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None
       self.explored=False


def is_leaf(node):
   if node.left==None and node.right==None:
         return True
   return False

def display(stack):
   stack1=[]
   for i in stack:
     stack1.append(i.value)
   print(stack1)

def print_root_leaf(node):
   if not node:
      return
   else:
      stack=[]
      test=node
      while True:
          if test:
             stack.append(test)
             test=test.left
          elif stack:
              test=stack[-1]
              if not test.explored:
                 test=test.right
                 stack[-1].explored=True
              elif test.explored:
                  if is_leaf(test):
                     display(stack)
                     stack.pop()
                     test=None
                  else:
                     stack.pop()
                     test=None    
          else:
             break
if __name__=="__main__":
   node=Node(12)
   node.left=Node(5)
   node.right=Node(1)
   node.left.left=Node(10)
   node.left.left.right=Node(6)
   node.left.left.left=Node(12)
   node.right.left=Node(18)
   node.right.right=Node(14)
   node.right.right.left=Node(21)
   node.right.right.right=Node(32)
   print_root_leaf(node)

