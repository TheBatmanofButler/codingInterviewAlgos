def insertBST(root, value):

	if root == None:
		return Node(value, None, None)

	if value < root:
		root.left = insertBST(tree.left, value)

	else:
		root.right = insertBST(tree.right, value)

	return root