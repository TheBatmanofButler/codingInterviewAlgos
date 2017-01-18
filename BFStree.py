def BFStree(root):

	if root == None: return None

	node = root
	q = deque()
	q.append(node)

	while len(q) > 0:
		node = q.popLeft()
		print node

		if node.left:
			q.append(node.left)

		if node.right:
			q.append(node.right)
