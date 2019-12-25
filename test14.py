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
    for obj in stack:
      stack1.append(obj.value)
    print(stack1)

def find_all_path(node):
   test=node
   stack=[]
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
            if is_leaf(stack[-1]):
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
   node.left=Node(23)
   node.right=Node(16)
   node.left.left=Node(21)
   node.left.right=Node(17)
   node.right.left=Node(21)
   node.right.right=Node(32)
   find_all_path(node)

   
                
        