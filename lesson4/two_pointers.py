#Recursion using 2 pointers
#eg: arr: [1,2,3,4,2]  Output = [ 2 4 3 2 1 ] its reversed
#other way to do it just have 2 pointers l = 0 and r = n-1 then swap it

def f(l,r):
    if l >= r: #base condition like SLIDING WINDOW if it greater than l the return
        return
    
    a[l], a[r] = a[r], a[l] #we are SWAPING the value 
    
    f(l+1 , r-1)
    
if __name__ == "__main__": 
    a:list[int] = [ 1, 2, 3, 4, 2]
    print(a)
    n:int = len(a)
    f(0, n-1)  
    print(a) 