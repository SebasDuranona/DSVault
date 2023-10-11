def quickSort(arr):
	if len(arr) <= 1:
		return arr

	# Step 1: Choose a pivot element (in this case, the middle element)
	pivot = arr[len(arr) // 2]

	# Step 2: Partition the element into three sub-arrays
	left = [x for x in arr if x < pivot] # Elements less than the pivot
	middle = [x for x in arr if x == pivot] # Elements equal to the pivot
	right = [x for x in arr if x > pivot] # Elements greater than the pivot

	# Step 3: Recursively apply Quick Sort to the left and right sub-arrays
	left_sorted = quickSort(left)
	right_sorted = quickSort(right)

	# Step 4: Combine the sorted sub-arrays and the pivot to form the final sorted array
	return left_sorted + middle + right_sorted

# Example Usage

example = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted: ", example)
print("Sorted: ", quickSort(example))