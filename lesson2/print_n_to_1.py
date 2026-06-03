#Print in terms of N to 1
#eg: n=4 
#Output = 4 3 2 1

def f(i,n):
    if i < 1:
        return
    print (i)
    f(i-1,n)

if __name__ == "__main__": 
    n:int = 4
    f(n,n) 
    
#TC = O(n) funtction is called n number times
#SC = O(n) its stores in the internal space called stack space