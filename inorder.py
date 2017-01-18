def inorder(node):

	stack = []
	while len(stack) > 0 or node != null:

		if node != null:
			stack.append(node)
			node = node.left

		else:
			node = stack.pop()
			print node.data
			node = node.right