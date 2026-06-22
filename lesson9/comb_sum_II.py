'''
candidates:list[int] = [2,1,4,3,1]
target:int = [4]

Answer 
    - [2,1,1]
    - [1,3]
    - [4]
    - [3,1]

Output 
    - [1,1,2]  #Has to be in sorted order
    - [1,3]    # Avoid any duplicates
    - [4]
    
Way to Approach
    - once you take the index you move onO
    - After you append it still stores the duplicate so store them in SET
    - buT here we use the if condition to avoid the same combination
'''

def findCombination(ind:int, candidates:list[int], target:int, ans:list[int], combination:list[int]):
        if target == 0:
            ans.append(combination[:])
            return

        for i in range(ind, len(candidates)):

            # skip duplicates combinations
            if i > ind and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            combination.append(candidates[i])

            findCombination(
                i + 1,
                candidates,
                target - candidates[i],
                ans,
                combination
            )

            combination.pop()
    

if __name__ == "__main__": 
    candidates:list[int] = [2,1,4,3,1]
    candidates.sort()
    target:int = 4
    answer:list[int] = []
    print(findCombination(ind=0,candidates=candidates,target=target,ans=answer, combination=[]))
    print(answer)