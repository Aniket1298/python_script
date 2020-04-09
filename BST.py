class Node:
	def __init__(self,val,f=1):
		self.val=val        #Value of Node
		self.left=None      #Left Child
		self.right=None     #Right Child
		self.f=f			#frequency of the number 
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
	else:
		root.f+=1
def search(n,root):
	if root==None:
		print n,"is not present in the BST"
	elif n<root.val:
		search(n,root.left)
	elif n>root.val:
		search(n,root.right)
	else:
		print  n,"is present in the BST"
def inorder(root):    #Inorder traversal 
	if root==None:
		return
	inorder(root.left)
	for i in range(root.f):
		print root.val,
	inorder(root.right)
Root=Node(3)  #Defining ROot Node
l=[2,4,1,6,9,-1,0,5,5,4,1,1,1,1,4]
for i in l:
	insert(Node(i),Root)
print "Inorder Traversal:",inorder(Root)
print 
search(7,Root)
