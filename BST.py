class Node:
	def __init__(self,val):
		self.val=val        #Value of Node
		self.left=None      #Left Child
		self.right=None     #Right Child
def insert(node,root):
	if node.val<root.val:
		if root.left==None:
			root.left=node
		else:
			insert(node,root.left)
	elif  node.val>root.val:
		if root.right==None:
			root.right=node
		else:
			insert(node,root.right)
def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print root.val
	inorder(root.right)
Root=Node(3)  #Defining ROot Node
l=[2,4,1,6,9,-1,0,5]
for i in l:
	insert(Node(i),Root)
inorder(Root)
