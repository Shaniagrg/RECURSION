 
""""
Using loop

Eg: This is an idea about how it looks but the code won't work cuz the index is out of range
Instead start with [0,1] and append the value
f:list[int] = []
f[0] = 0
f[1] = 1
n:int = len(f)

for i in range(2,n,1):
    f[i] = f[i-1] + f[i-2]

"""

n = 10  # Total numbers desired orelse it will print until the computer runs out of space

# Pre-allocate a list of size n filled with zeros
f: list[int] = [0] * n

# Set your base cases
f[0] = 0
f[1] = 1

# Now you can safely use f[i] because the indices already exist
for i in range(2, n):
    f[i] = f[i-1] + f[i-2]

print(f)
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

"""
TC = O(n)
SC = O(n)
"""