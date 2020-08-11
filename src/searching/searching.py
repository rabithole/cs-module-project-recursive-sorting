# TO-DO: Implement a recursive implementation of binary search
import pdb
def binary_search(arr, target, left, right):
	if left > right:
		return -1
	else: 
		mid = (left + right) // 2

		if arr[mid] == target:
			return mid

		elif arr[mid] < target:
			return binary_search(arr, target, mid + 1, right)

		else:
			return binary_search(arr, target, left, mid - 1)
	# base case
	# Stop when we find the target
	# or we have searched the whole array. if left > right
	# how do we move closer to the base case. 
    # Your code here
arr = [3, 4, 16, 29, 39, 40, 56, 100, 200, 300]
print(binary_search(arr, 100, 0, len(arr)-1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
	pass
    # Your code here



list = [5, 16, 36, 36, 69, 20, 23]

# pdb.set_trace()
def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])

result = sum_list(list)
# print(result)

# def print_to_zero(n):
#     print(n)
#     if n == 0: # base case
#         return
#     return print_to_zero(n - 1) # recursive case

# result = print_to_zero(10)
# print(result)