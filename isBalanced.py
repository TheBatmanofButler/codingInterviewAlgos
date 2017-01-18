def isBalanced(root):
	if root == None:
		return 0

	leftH = isBalanced(root.left)
	if leftH == -1:
		return -1

	rightH = isBalanced(root.right)
	if rightH == -1:
		return -1

	diff = leftH - rightH
	if abs(diff) > 1:
		return -1

	return 1 + max(leftH, rightH)