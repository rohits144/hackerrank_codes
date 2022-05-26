def minimumSwaps(arr):
    counter = 0
    for i in range(len(arr)):
        while(i+1 != arr[i]):
            swap_index = arr[i]-1
            swap_index_val = arr[swap_index]
            arr[i], arr[swap_index] = swap_index_val, arr[i]
            counter+=1
    return counter   

print(minimumSwaps([1,3,5,2,4,6,7]))