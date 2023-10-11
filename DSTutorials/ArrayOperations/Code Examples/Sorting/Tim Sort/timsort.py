# Insertion Sort: Sorts a portion of the array in-place
def insertionSort(arr, left = 0, right = None):
	if right is None:
		right = len(arr) - 1

	for i in range(left + 1, right + 1):
		key_item = arr[i]
		j = i - 1
		while j >= left and arr[j] > key_item:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key_item

# Merge: Merges two sorted arrays into a single sorted array
def merge(left, right):
	if not left:
		return right

	if not right:
		return left

	if left[0] < right[0]:
		return [left[0]] + merge(left[1:], right)

	return [right[0]] + merge(left, right[1:])

# Timsort: Combines insertion sort and merge sort for efficient sorting
def timSort(arr):
	# Minimum run size for insertion sort
	min_run = 32
	n = len(arr)

	# Apply insertion sort to small chunks of the array
	for i in range(0, n, min_run):
		insertionSort(arr, i, min((i + min_run - 1), n - 1))

	size = min_run
	while size < n:
		for start in range(0, n, size * 2):
			midpoint = min((start + size - 1), (n - 1))
			end = min((start + size * 2 - 1), (n - 1))

			# Merge the sorted chunks
			left = arr[start : midpoint + 1] 
			right = arr[midpoint + 1 : end + 1]
			merged_array = merge(left, right)
			arr[start : start + len(merged_array)] = merged_array

		size *= 2

# Example Usage

example = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted: ", example)
timSort(example)
print("Sorted: ", example)