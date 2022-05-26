class Solution:
    def subArraySum(self,arr, n, s): 
        
        if s in arr:
            return [arr.index(s)+1, arr.index(s)+1]
            
        for i in range(len(arr)):
           sum = arr[i]
           
           for j in range(i+1, len(arr)):
               sum = sum + arr[j]
               if sum < s:
                   continue
               elif sum == s:
                   return [i+1, j+1]
               else:
                   break
               
        return [-1]