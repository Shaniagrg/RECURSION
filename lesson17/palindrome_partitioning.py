'''
S = "aabb"

Output: [
    ['a', 'a', 'b', 'b']
    ['a' , 'a', 'bb']
    [ 'aa', 'b', 'b']
    ['aa', 'bb' ]

Primary Task 
    - is to partition
    - Every string has to be Palindrome
    - partition can be anywhere

'''

def isPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def backtrack(index, path):
    if index == len(s):
        ans.append(path[:])
        return

    for end in range(index, len(s)):

        # Only continue if substring is palindrome
        if isPalindrome(s, index, end):

            path.append(s[index:end + 1])

            backtrack(end + 1, path)

            path.pop()


s = "aabb"

ans = []

backtrack(0, [])

print(ans)