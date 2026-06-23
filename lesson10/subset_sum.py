'''
nums:list[int] = [3,1,2]
n:int = 3

Subset sum
    - 0
    - 3
    - 1
    - 2
    - 3 + 1 = 2
    - 3 + 2 = 5
    - 1 + 2 = 3
    - 3 + 1 + 2 = 6

Return the output in all ascending order
Output = 0 1 2 3 3 4 5 6
    
'''

def subset_sum(ind:int, sum:int, arr:list[int], n:int, sumSubset:list[int]):
    if ind == n:
        sumSubset.append(sum)
        return
    
    # Take
    subset_sum(ind+1, sum + arr[ind], arr, n, sumSubset)
    
    # Not Take
    subset_sum(ind+1, sum, arr, n, sumSubset)
    
if __name__ == "__main__": 
    nums:list[int] = [3,1,2]
    n:int = len(nums)
    ans = []

    subset_sum(0, 0, nums, n, ans)

    ans.sort()

    print(ans)
    
    