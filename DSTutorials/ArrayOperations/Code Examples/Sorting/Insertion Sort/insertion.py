def insertionSort(arr):
	# Traverse the array from the second element
	for i in range(1, len(arr)):
		# Store the current element as the 'key' to be inserted
		key = arr[i]
		# Variable j will point to the element just before the 'key'
		j = i-1
		# Move the elements of the array that are greater than 'key' one position ahead of their current position
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1

		# Insert the 'key' into its correct position in the sorted part of the array
		arr[j + 1] = key


# Example Usage

example = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted: ", example)
insertionSort(example)
print("Sorted: ", example)