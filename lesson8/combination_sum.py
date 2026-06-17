'''
You can use the same value multiple times to get target
eg: input = [3,4,1,2] target 4
Output = [4]  
         [1,1,1,1]  
         [1,1,2]  
         [2,2]
    Here you added 1 and 2 multiple time to get the targets
'''

def findCombination(ind:int, target:int, ans:list[int], combination:list[int]):
    if ind == len(nums):
        if target == 0:
            ans.append(list(combination))
        return
    
    if nums[ind] <= target:
            combination.append(nums[ind])  # Add the current element to the combination
            findCombination(ind, target - nums[ind], ans, combination)  # Continue with the same index to allow repeated elements
            combination.pop()
    
    findCombination(ind + 1, target, ans, combination)
    

if __name__ == "__main__": 
    nums:list[int] = [2,3,6,7]
    k:int = 7
    answer:list[int] = []
    print(findCombination(ind=0,target=k,ans=answer, combination=[]))
    print(answer)