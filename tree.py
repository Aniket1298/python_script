class Tree:
	def __init__(self,edges,n):
		self.tree=[]
		self.nodes=n
		f=[0]*(n+1)
		self.leaves=[] #leaf nodes
		for i in range(n+1):
			self.tree.append([])
		for u,v in edges:
			self.tree[u].append(v)
			self.tree[v].append(u)
			f[u]+=1
			f[v]+=1
		for i in range(len(f)):
			if f[i]==1:
				self.leaves.append(i)
				
	def bfs(self,root=1):
		q=[root]  # 1 as default  Root Node
		l=[]
		visited=[0]*(self.nodes+1)
		visited[root]=1
		while len(q)!=0:
			layer=[]
			for i in q:
				layer.append(i)
			l.append(layer)
			t=[]
			while len(q)!=0:
				x=q.pop(0)
				visited[x]=1
				for i in self.tree[x]:
					if visited[i]==0:
						t.append(i)
			q=t[::]
		return l
