'''
Formula to rememer
    - take 
    - not take

f(ind,[])
    if (ind >= n )
        print ([])
        return
    
    [].add(arr[i])
    
    f(ind+1, [])          //take
    
    [].remove(arr[i])
    
    f(ind+1, [])          //not take

'''

def print_subsequnce(ind:int, arr:list[int], n:int):
    if ind >= n:
        print(arr)
        return
    
    arr.append(nums[ind])
    
    print_subsequnce(ind+1, arr,n)
    
    arr.pop()
    
    print_subsequnce(ind+1, arr,n)

if __name__ == "__main__": 
    nums:list[int] = [3,1,2]
    n:int = len(nums)
    print_subsequnce(ind=0,arr=[],n=n)
   