#Print linearly from n to 1
#eg: n = 3 output: 3 2 and 1
#don't use -1 like f(i-1,n)

def f(i,n):
    if i > n:  #base condition: print till n number of times which is 3
        return
    f(i+1,n)  #call function first cuz if you prin tit will print 1 2 and 3
    print(i) #after function when you print it will print 3 2 and 1
    #once its print the fucntion is executed and go back
if __name__ == "__main__": 
    n:int = 3
    f(1,n) 
    
#TC = O(n) funtction is called n number times
#SC = O(n) its stores in the internal space called stack space