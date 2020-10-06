# TO-DO: Implement a recursive implementation of binary search
list1 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

def binary_search(arr, target, start, end):
	if start > end:
		return f'It is not here!'
	else: 
		mid = (start + end) // 2

		if arr[mid] == target:
			return f'What your searching for is here!'

		elif arr[mid] < target:
			return binary_search(arr, target, mid + 1, end)

		else:
			return binary_search(arr, target, start, mid - 1)

print('')
print(binary_search(list1, 2, 0, len(list1) - 1))
print('')


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

