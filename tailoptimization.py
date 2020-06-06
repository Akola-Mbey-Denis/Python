def factorial(n,acc):
    if n==0:
        return acc
    else:
        return  factorial(n-1,acc*n) 

def compute_factorial(n):
    return factorial(n,1)



if __name__ =="__main__":
    print(compute_factorial(5))
