#Recursion Using 1 pointer
#eg arr = [1, 2, 3, 4] Output = [4, 3, 2, 1]
#idea is when pointer is at index 0 we want to swap with the end index which will be n - i - 1
#swap happenes between index 0 and index n-i-1

def f(i):
    if i >= n/2: #Base condition: once its in middle we return
        return
    
    temp:int = array[i]        #swap
    array[i] = array[n-i-1]    #swap
    array[n-i-1] = temp        #swap
    
    f(i+1)
    
if __name__ == "__main__": 
    array:list[int] = [ 1, 2, 3, 4]
    print(array)
    n:int = len(array)
    f(0)  
    print(array) 
