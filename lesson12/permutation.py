def recurPermute(nums: list[int], ds: list[int], ans: list[list[int]], freq: list[bool]):

    if len(ds) == len(nums):
        ans.append(ds[:])
        return

    for i in range(len(nums)):

        if not freq[i]:

            freq[i] = True
            ds.append(nums[i])

            recurPermute(nums, ds, ans, freq)

            ds.pop()
            freq[i] = False


if __name__ == "__main__":

    nums = [1, 2, 3]

    ans = []
    ds = []
    #For permutations, we need to know which numbers have already been used in the current permutation.
    #This case we start with 3 [False, False, False]. 
    #once the value is taken it will look like this [True, False, False]
    freq = [False] * len(nums)

    recurPermute(nums, ds, ans, freq)

    print(ans)