def mergeSort(arr):
	if len(arr) <= 1:
		return arr

	# Split the array in 2 halves
	mid = len(arr) // 2
	left_half = arr[:mid]
	right_half = arr[mid:]

	# Recursively sort both halves
	left_half = mergeSort(left_half)
	right_half = mergeSort(right_half)

	# Merge the sorted halves
	return merge(left_half, right_half)

def merge(left, right):
	result = []
	left_idx, right_idx = 0, 0

	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx] < right[right_idx]:
			result.append(left[left_idx])
			left_idx += 1

		else:
			result.append(right[right_idx])
			right_idx += 1

	# Append the remaining elements from both lists (if any)
	result.extend(left[left_idx:])
	result.extend(right[right_idx:])

	return result

# Example Usage

example = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted: ", example)
print("Sorted: ", mergeSort(example))
