
def maxSubarrayProduct(arr, n):

	# Initializing result
	result = arr[0]

	for i in range(n):
		print("first loop i = ", i)
		mul = arr[i]
		print("mul =",mul)
		# traversing in current subarray
		for j in range(i + 1, n):
			print("second loop j = ", j)
			# updating result every time
			# to keep an eye over the maximum product
			result = max(result, mul)
			mul *= arr[j]
			print("result = ", result, "mul = ", mul)
		# updating the result for (n-1)th index.
		result = max(result, mul)
		print("result = ", result)
	
	return result

# Driver code
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print("Maximum Sub array product is" , maxSubarrayProduct(arr, n))

