'''

Count the subsequence with the sum = k  

arr:list[int] = [1,2,1]
k = 2
output = 2 (cuz the sum of k 2 comes from [1,1] and [2])

'''

def sum_k(ind:int, n:int, s:int) -> bool:
    
    # Base Condition
    if ind == n:
        # Target sum found: return 1 to count this valid subsequence
        if s == sum:
            return 1
        # Target sum not found: return 0
        else:
            return 0 
    
    # TAKE PATH 
    s += nums[ind]
    
    #Find the count from the TAKE path (stored in l).
    l:int =  sum_k(ind+1,n,s) 
        
    #Backtrack
    s -= nums[ind]  # Undo the choice to reset state for the next path
    
    # NOT TAKE PATH
    #Find the count from the NOT TAKE path (stored in in r)
    r:int = sum_k(ind+1,n,s) 
    
    #Return the sum of both paths (l + r) back to the parent call
    return l + r 

if __name__ == "__main__": 
    nums:list[int] = [1,2,1]
    sum:int = 2
    n:int = len(nums)
    print(sum_k(ind=0,n=n,s=0))