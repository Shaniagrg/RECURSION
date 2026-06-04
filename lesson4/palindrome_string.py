#Check if the string is PALINDROME or not
#PALINDROME: A string on revesal reads / stays the exact same
#eg: string = "MADAM"  reverse = "MADAM"
#eg integer = "11211"  reverse = "11211"

def f(i):
    #We are not swapping just check if the swapping value is same or not cuz even when we swap it will still be the same
    if i >= n/2:    #base condition: once its in the middle then everything is True
        return True
    if s[i] != s[n-i-1]:  #if the swaping value is different than return False
        return False   
    
    return f(i+1)

if __name__ == "__main__": 
    s:str = "MADAM"
    n:int = len(s)
    print(f(0))
    
