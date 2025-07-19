print("Hello, JOSEPHINE! you're back in python")
def fact(a: int):
    if a == 0:
        return 1
    else:
        return a * fact(a-1)
    
print(fact(5))