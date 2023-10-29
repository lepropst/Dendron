
import graphviz

class BSTNode:
	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val

	def print_tree(self):
		dot = graphviz.Digraph()
		dot.node(str(self.val))

		def add_nodes_edges(node):
			if node.left:
				dot.node(str(node.left.val))
				dot.edge(str(node.val), str(node.left.val))
				add_nodes_edges(node.left)
			if node.right:
				dot.node(str(node.right.val))
				dot.edge(str(node.val), str(node.right.val))
				add_nodes_edges(node.right)

		add_nodes_edges(self)
		dot.render('binary_tree', view=True, format='png')

	def insert(self, val):
		if not self.val:
			self.val = val
			return
		if self.val == val:
			return
		if val < self.val:
			if self.left:
				self.left.insert(val)
				return
			self.left = BSTNode(val)
			return
		if self.right:
			self.right.insert(val)
			return
		self.right = BSTNode(val)
	def delete(self, val):
		print(f"deleting {val} using right sub-tree")
		if self == None:
			return self
		if self.right == None:
			return self.left
		if self.left == None:
			return self.right
		if val < self.val:
			if self.left:
				self.left = self.left.delete(val)
			return self
		if val > self.val:
			if self.right:
				self.right = self.right.delete(val)
			return self
		min_larger_node = self.right
		while min_larger_node.left:
			min_larger_node = min_larger_node.left
		self.val = min_larger_node.val
		self.right = self.right.delete(min_larger_node.val)
		return self

	def inorder(self, vals):
		if self.left is not None:
			self.left.inorder(vals)
		if self.val is not None:
			vals.append(self.val)
		if self.right is not None:
			self.right.inorder(vals)
		return vals
	def preorder(self, vals):
		if self.val is not None:
			vals.append(self.val)
		if self.left is not None:
			self.left.preorder(vals)
		if self.right is not None:
			self.right.preorder(vals)
		return vals
	def postorder(self, vals):
		if self.left is not None:
			self.left.postorder(vals)
		if self.right is not None:
			self.right.postorder(vals)
		if self.val is not None:
			vals.append(self.val)
		return vals


	def print_tree(self, string):
		dot = graphviz.Digraph(comment=string)
		dot.node(str(self.val))

		def add_nodes_edges(node):
			if node.left:
				dot.node(str(node.left.val))
				dot.edge(str(node.val), str(node.left.val))
				add_nodes_edges(node.left)
			if node.right:
				dot.node(str(node.right.val))
				dot.edge(str(node.val), str(node.right.val))
				add_nodes_edges(node.right)

		add_nodes_edges(self)
		dot.render(string, view=True, format='png', directory="./graph_images/binary-search-tree")

