'''
Print ANY subsequence whose sum array is sum

arr:list[int] = [1,2,1]
sum:int = 2

Output = [1,1] and [2]
BUT 
Print only 1 either [1,1] ----- OR ---- [2]

Base condition 
    - when u find the sum while TAKE then no need to proceed with NOT TAKE
'''

def sum_k(ind:int, arr:list[int], n:int, s:int) -> bool:
    
    # Base Condition
    if ind == n:
        # ---- Condition satisfied ----
        if s == sum:
            print(arr)
            return True
        # ---- Condition not satisfied ----
        else:
            return False
    
    # TAKE PATH 
    arr.append(nums[ind])
    s += nums[ind]
    
    #Return if True and no need to move forward
    if sum_k(ind+1, arr,n,s) == True:
        return True
    
    # BACKTRACK

    s -= nums[ind]
    arr.pop()
    
    # NOT TAKE PATH
    if sum_k(ind+1, arr,n,s) == True:
        return True
    
    #if both Take/Not take doesn't return True then you return False
    return False

if __name__ == "__main__": 
    nums:list[int] = [1,2,1]
    sum:int = 2
    n:int = len(nums)
    sum_k(ind=0,arr=[],n=n,s=0)