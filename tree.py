class Tree: 
	def __init__(self, cargo, left=None, right=None):
		self.cargo=cargo
		self.left=left
		self.right=right

	def __str__(self):
		return str(self.cargo)


left=Tree(2)
right=Tree(3)

tree=Tree(1, left, right);

print tree


#traversing trees
def total(tree):
	if tree == None: return 0
	return total(tree.left) + total(tree.right)+tree.cargo
print total(tree)

# preorder traverse. from root to children
def print_tree(tree):
	if tree == None: return
	print tree.cargo, 
	print_tree(tree.left)
	print_tree(tree.right)
print "preorder-"
print_tree(tree) 

# postorder traverse, from left, right 
def print_tree_postorder(tree):
	if tree == None: return
	print_tree_postorder(tree.left) #what's the difference between print tree.right? 	print tree.right
	print_tree_postorder(tree.right)
	print tree.cargo,
print "\npost order-"
print_tree_postorder(tree)

# inorder traverse, from left, root, right
def print_tree_inorder(tree):
	if tree == None: return
	print_tree_inorder(tree.left)
	print tree.cargo,
	print_tree_inorder(tree.right)
print "\ninoder-"
print_tree_inorder(tree)





