# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
	# elements = len(arrA) + len(arrB)
	merged_arr = []

	a = 0
	b = 0

	while a < len(arrA) and b < len(arrB):
		if arrA[a] < arrB[b]:
			merged_arr.append(arrA[a])
			a += 1
			print(merged_arr)
		else:
			merged_arr.append(arrB[b])
			b += 1
		# print(merged_arr)

	if a < len(arrA):
		merged_arr.extend(arrA[a:])
	if b < len(arrB):
		merged_arr.extend(arrB[b:])

	return merged_arr

print('')
first = [2, 5, 16, 39, 45, 50, 68]
sec = [14, 26, 35, 46, 50, 60, 74, 83]
print('MERGE', merge(first, sec))
print('')

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
	# base case: stop splitting the arrays in half when the arrays reach a length of 1
	if len(arr) > 1:
		left = merge_sort(arr[0 : len(arr) // 2]) # split from 0.
		right = merge_sort(arr[len(arr) // 2 : ]) # to end of array.
		arr = merge(left, right)
	return arr

print('')
thisList = [3, 45, 1, 50, 29, 40, 28, 36, 200, 4, 34, 89, 29, 59]
print('MERGE SORT', merge_sort(thisList))
print('')

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
	pass
    # Your code here

