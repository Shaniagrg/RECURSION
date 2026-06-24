'''
nums = [1,2,2]

answer must not contain duplicate subsets

Output:
    [
    [],
    [1],
    [2],
    [1,2],
    [2,2],
    [1,2,2]
    ]

'''

def findSubsets(ind: int, nums:list[int], ds: list[int], ans:list[list[int]]):
    ans.append(ds[:])

    for i in range(ind, len(nums)):
        #Skip Duplicate
        if i != ind and nums[i] == nums[i - 1]:
            continue

        ds.append(nums[i])

        findSubsets(i + 1, nums, ds, ans)

        ds.pop()

if __name__ == "__main__": 
    nums = [1, 2, 2]
    nums.sort()

    ans = []

    findSubsets(0, nums, [], ans)

    print(ans)