def postorder(root):

	stack = []
	node = root
	lastVisitedNode = None

	while len(stack) > 0 or node != None:

		if node != None:
			stack.append(node)
			node = node.left

		else:
			peekNode = stack.peek()
			if peekNode.right != None and lastVisitedNode != peekNode.right:
				node = peekNode.right

			else:
				print peekNode
				lastVisitedNode = stack.pop()