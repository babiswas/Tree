class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None
      self.level=0

  def inorder(self):
      if self:
        if self.left:
           self.left.inorder()
        print(self.value)
        if self.right:
           self.right.inorder()

  def top_view(self):
      queue=[]
      d={}
      queue.append(self)
      while queue:
          m=queue.pop(0)
          if m.level not in d:
             d[m.level]=[]
          d[m.level].append(m.value)
          if m.left:
            queue.append(m.left)
          if m.right:
            queue.append(m.right)
      print("Top view of the tree")
      for i in sorted(d.keys()):
        print(d[i][0])
      print("Bottom view of the tree")
      for i in sorted(d.keys()):
        print(d[i][-1])
          

  def insert(self,value):
      if self.value>value:
          if self.left:
             self.left.insert(value)
          else:
             self.left=Node(value)
             self.left.level=self.level-1
      elif self.value<value:
          if self.right:
             self.right.insert(value)
          else:
             self.right=Node(value)
             self.right.level=self.level+1
      else:
        print("Duplication not allowed")

if __name__=="__main__":
   node=Node(12)
   node.insert(23)
   node.insert(25)
   node.insert(21)
   node.insert(27)
   node.insert(18)
   node.insert(14)
   node.insert(20)
   node.insert(5)
   node.insert(10)
   node.insert(11)
   node.insert(7)
   node.insert(1)
   print("Top view of the course is:")
   node.top_view()
   print("Inorder traversal of the course is:")
   node.inorder()


   
