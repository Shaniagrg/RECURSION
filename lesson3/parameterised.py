# Calling function using argument and parameter

def f(i:int, sum:int):
    if i < 1: #base condition once it reach n it will end
        print(sum) 
        return
    f(i-1,sum+i) #call function again and change the sum value

if __name__ == "__main__": 
    n:int = 3
    f(n,0) 