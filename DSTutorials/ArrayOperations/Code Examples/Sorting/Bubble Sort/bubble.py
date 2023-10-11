def bubbleSort(arr):
	n = len(arr)

	# Traverse through all elements in the array
	for i in range(n):
		# Flag to detect if any swaps have occured. This will help optimize the algorithm
		swapped = False

		for j in range(0, n - i - 1):
			# Compare adjacen elements
			if arr[j] > arr[j+1]:
				# Swap elements
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		# If no two elements were swapped in the inner loop, we know the array is sorted, so we stop
		if not swapped:
			break

# Example Usage

example = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted: ", example)
bubbleSort(example)
print("Sorted: ", example)