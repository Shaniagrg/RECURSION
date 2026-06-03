#Print Name n times using recursion

def f(i,n):
    if i > n:  #base condition: we only print raj n times which is 3 and once done return
        return
    print ("raj")
    f(i+1,n) 

if __name__ == "__main__": 
    n:int = 3
    f(1,n) 
    
#TC = O(n) cuz you are calling function n number of times
#SC = O(n) cuz even we are not using any space to store anything the computer is using internal space called "stack space" where the functions are stacked until return