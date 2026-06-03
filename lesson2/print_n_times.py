#Print Name n times using recursion

def f(i,n):
    if i > n:  #base condition: we only print raj n times which is 3 and once done return
        return
    print ("raj")
    f(i+1,n) 

if __name__ == "__main__": 
    n:int = 3
    f(1,n) 