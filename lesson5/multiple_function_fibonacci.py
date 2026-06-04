#Multiple function Recursion

def f(n):
    if n <=1: #base condition
        return n
    left:int = f(n-1)
    right:int = f(n-2)
    print(left,right,left+right) #to check what it returns 
    return left + right  #returns like backtracking

if __name__ == "__main__": 
    f(4)
    