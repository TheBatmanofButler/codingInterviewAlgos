def binary_search(arr, value):

	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = (low + high) / 2
		if value < arr[mid]:
			high = mid - 1
		elif value > arr[mid]:
			low = mid + 1
		else:
			return True

	return False