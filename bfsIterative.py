def bfsIterative(root, val):

	visited = set()
	node = root
	queue = deque(node)

	while len(queue) > 0:
		node = queue.popLeft()

		if node in visited:
			continue

		visited.add(node)
		if node == val:
			return True

		for i in node.adj:
			if i not in visited:
				queue.append(i)

	return False