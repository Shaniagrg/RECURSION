#Print Linearly from 1 to n
def f(i,n):
    if i > n: #base condition: print n times which is 3 for this example
        return
    print (i)
    f(i+1,n)

if __name__ == "__main__": 
    n:int = 3
    f(1,n) 

#TC = O(n) funtction is called n number times
#SC = O(n) its stores in the internal space called stack space

#check