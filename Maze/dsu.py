from random import randrange

class DSU:
	def __init__(self):
		self.parent = []

	def find(self, u):
		if u not in self.parent:
			self.parent[u] = u

			return u

		# Iterative path compression
		stack = []
		while u != self.parent[u]:
			stack.append(u)
			u = self.parent[u]
		for v in stack:
			self.parent[v] = u

		return u

	def unite(self, u, v):
		root_u, root_v = self.find(u), self.find(v)

		if root_u != root_v:
			if randrange(2) == 0:
				self.parent[root_u] = root_v
			else:
				self.parent[root_v] = root_u
