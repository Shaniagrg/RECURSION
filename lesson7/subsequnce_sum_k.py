'''
Printing subsequence whose sum is k

arr:list[int] = [1,2,1]
sum:int = 2

Output = [1,1] and [2]

use the same concept take and not take

Base condition is different cuz we looking for sum
    -   if i == n
            if s == sum
'''

def sum_k(ind:int, arr:list[int], n:int, s:int):
    # Base Case: Always return when we reach the end of the array
    if ind == n:
        if s == sum:
            print(arr)
        return
    
    # TAKE PATH 
    arr.append(nums[ind])
    
    # Fixed: Use nums[ind], not arr[ind]
    s += nums[ind]
    sum_k(ind+1, arr,n,s) 
    
    # BACKTRACK
    # We must subtract the value BEFORE popping it,
    s -= nums[ind]
    arr.pop()
    
    # NOT TAKE PATH
    sum_k(ind+1, arr,n,s)

if __name__ == "__main__": 
    nums:list[int] = [1,2,1]
    sum:int = 2
    n:int = len(nums)
    sum_k(ind=0,arr=[],n=n,s=0)