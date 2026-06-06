#Print all Permutation of string/array using extra space complexity

def calculate_permutations(self, start, nums, result):
        # Base Case: If the start pointer reaches the end, 
        # we have a complete permutation.
        
        if start == len(nums):
            result.append(nums[:])  # nums[:] creates a fresh copy of the current order
            return
        
        for i in range(start, len(nums)):
            # 1. Swap the element at 'start' with the element at 'i'
            nums[start], nums[i] = nums[i], nums[start]
            
            # 2. Recursively find permutations for the rest of the array
            self.calculate_permutations(start + 1, nums, result)
            
            # 3. Backtrack: Swap them back to restore the original order
            nums[start], nums[i] = nums[i], nums[start]
        
        return result

def permute(self, nums: list[int]) -> list[list[int]]:
    result = []
    return self.calculate_permutations(0, nums, result)
