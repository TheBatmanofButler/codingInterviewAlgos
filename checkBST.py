def checkBST(root):

	stack = []
	lastVisitedNode = None
	node = root

	while len(stack) > 0 or node != None:
		if node != None:
			stack.push(node)
			node = node.left

		else:
			node = stack.pop()
			if lastVisitedNode != None and node < lastVisitedNode:
				return False

			lastVisitedNode = node
			node = node.right

	return True