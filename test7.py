class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def height(node):
   count=0
   if not node:
      return 0
   else:
     queue=[]
     queue.append(node)
     while queue:
        q_len=len(queue)
        count=count+1
        while q_len:
           m=queue.pop(0)
           if m.left:
             queue.append(m.left)
           if m.right:
             queue.append(m.right)
           q_len=q_len-1
     return count

def diameter(node):
   left=0
   right=0
   h_right=0
   h_left=0
   if not node:
      return 0
   else:
      if node.right:
         right=diameter(node.right)
      if node.left:
         left=diameter(node.left)
      if node.right:
         h_right=height(node.right)
      if node.left:
         h_left=height(node.left)
      return max(h_right+h_left+1,max(right,left))

if __name__=="__main__":
   node=Node(12)
   node.left=Node(13)
   node.right=Node(17)
   node.left.left=Node(12)
   node.left.right=Node(18)
   node.left.left.left=Node(19)
   node.left.left.left.left=Node(21)
   node.left.left.left.left.left=Node(10)
   node.right.left=Node(100)
   node.right.right=Node(50)
   print(diameter(node))



   