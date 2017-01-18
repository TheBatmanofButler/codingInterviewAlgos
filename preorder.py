def preorder(root):
	
	if root is None:
		return None

	else:
		stack = []
		stack.append(root)
		while len(stack) > 0:
			node = stack.pop()

			print node
			if node.right:
				stack.append(node.right)

			if node.left:
				stack.append(node.left)