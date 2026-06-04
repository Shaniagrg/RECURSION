#functional: when you want the fucntion to return something not print
# eg: n = 3 then output will be 1+2+3 = 6 so at the end when u add you get 6 
def f(n):
    if n == 0:
        return 0  
    return n + f(n-1) 

if __name__ == "__main__": 
    n:int = 3
    print(f(n)) 