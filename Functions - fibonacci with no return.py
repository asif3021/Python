def fibonacci(f):
    """Print a fibonacci series up to n."""
    a,b=0,1
    while a<f:
        print(a,end=" ")
        a,b=b,a+b
