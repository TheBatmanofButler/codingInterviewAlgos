def merge_sort(arr):

	if len(arr) <= 1:
		return arr

	mid = len(arr) / 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])

	return merge(left, right)

def merge(left, right):

	if not left:
		return right

	elif not right:
		return left

	else:
		if left[0] < right[0]:
			return [left[0]] + merge(left[1:], right)

		else:
			return [right[0]] + merge(left, right[1:])