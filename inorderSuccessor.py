def inorderSucc(root):

	node = root
	stack = []
	prev = None

	while len(stack) > 0 or node != None:
		
		if node != null:
			stack.push(node)
			node = node.left

		else:
			node = stack.pop()
			if prev == None:
				prev = node
			else:
				if prev == root:
					return node
				else:
					prev = node
			node = node.right