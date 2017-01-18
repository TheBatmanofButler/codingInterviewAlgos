def dfsIterative(node, val):

	visited = set()
	stack = [node]

	while len(stack) > 0:
		node = stack.pop()
		if node in visited:
			continue

		visited.add(node)
		if node == val:
			return True

		for i in node.adj:
			if i not in visited:
				stack.append(i)

	return False