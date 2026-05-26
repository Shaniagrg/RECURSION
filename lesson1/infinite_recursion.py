# The condition where it will run infitnite anount of time until the comouter memory is full 

count:int = 0 

def f() -> None: 

    print(1) 

    f() 

if __name__ == "__main__": 

    f() 