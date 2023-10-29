
class BSTNode:
	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val


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

	def print(self):
		stri = []
		for node in self.postorder([]):
			if node is str:
				stri.append(node.upper)
			else:
				stri.append(node)
		print(stri)
		stri =[]
		for node in self.preorder([]):
			if node is str:
				stri.append(node.upper)
			else:
				stri.append(node)
		print(stri)
		stri =[]
		for node in self.inorder([]):
			if node is str:
				stri.append(node.upper)
			else:
				stri.append(node)
		print(stri)
def main():
	items = [55, 34, 20, 48, 15, 24, 30, 65, 60, 73, 56, 64, 70, 68, 72]
	bst = BSTNode()
	print(len(items))
	for itm in items:
		bst.insert(itm)
	


# 24, 73, 34, 65, 55

if __name__ == "__main__":
	main()
