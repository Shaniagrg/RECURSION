#Print linearly from 1 to n (But by BACK TRACK)
#Without using +1 in f(i+1,n)

def f(i,n):
    if i < 1:
        return #base condition: only print till n which is 1 2 and 3
    f(i-1,n) #call the function first cuz if you print first it wll print 3 2 and 1
    print(i) #after calling function print to print in serial 1 2 and 3

if __name__ == "__main__": 
    n:int = 3
    f(n,n) 
    
#TC = O(n) funtction is called n number times
#SC = O(n) its stores in the internal space called stack space
