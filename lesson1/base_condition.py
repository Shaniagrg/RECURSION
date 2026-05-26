# The condition where you stop calling the function 

count:int = 0 

def f() -> None: 

    global count # It showed error without this BUT avoid using global in RECURION instead pass "count" as argument f(0) parameter f(count:int) 

    if count == 4: 

        return 

    print(count) 

    count += 1 

    f() 

if __name__ == "__main__": 

    f() 