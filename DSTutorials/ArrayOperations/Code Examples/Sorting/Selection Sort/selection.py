def selectionSort(arr):
	n = len(arr)

	for i in range(n):
		# Find the minimum element in the unsorted portion
		min_index = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_index]:
				min_index = j

		# Swap the found minimum element with the first element
		arr[i], arr[min_index] = arr[min_index], arr[i]


# Example Usage

example = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted: ", example)
selectionSort(example)
print("Sorted: ", example)