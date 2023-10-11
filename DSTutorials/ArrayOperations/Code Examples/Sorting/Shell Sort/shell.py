def shellSort(arr):
	n = len(arr)
	gap = n // 2 # Start with a large gap and reduce it until it becomes 1

	while gap > 0:
		for i in range(gap, n):
			temp = arr[i]
			j = i
			# Move elements that are greater than temp by the gap
			while j >= gap and arr[j - gap] > temp:
				arr[j] = arr[j - gap]
				j -= gap
			arr[j] = temp
		gap //= 2 # Reduce the gap

# Example Usage

example = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted: ", example)
shellSort(example)
print("Sorted: ", example)