from dsu import DSU

class Solver:
	def __init__(self):
		self.dsu = DSU()

	def solve(self, maze=None, point=None, path=None):
		if path is not None:
			maze = []
			with open(path, "r") as file:
				for line in file:
					maze.append(line.strip())

		return True
