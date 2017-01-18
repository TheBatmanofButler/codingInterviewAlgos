def searchBST(root, key):

	current = root

	while current != None:
		if key == current:
			return current

		elif key < current:
			current = current.left

		else:
			current = current.right

	return None