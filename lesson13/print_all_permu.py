'''
nums:list[int] = [1,2,3]
n:int = 3

Use SWAP not extra ds/map to store permutation

Output = 
    [[1, 2, 3]
    [1, 3, 2], 
    [2, 1, 3], 
    [2, 3, 1], 
    [3, 2, 1], 
    [3, 1, 2]]
'''

def recurPermute(index: int, nums: list[int], ans: list[list[int]]):

    if index == len(nums):
        ans.append(nums[:])
        return

    for i in range(index, len(nums)):
    
        #This restores the array before trying the next choice.
        nums[index], nums[i] = nums[i], nums[index]

        recurPermute(index + 1, nums, ans)

        nums[index], nums[i] = nums[i], nums[index]


if __name__ == "__main__":

    nums = [1, 2, 3]

    ans = []

    recurPermute(0, nums, ans)

    print(ans)