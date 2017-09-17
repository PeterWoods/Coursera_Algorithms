# Uses python3

def calc_fib(n):

    i= 3
    fib = [0,1,1]

    if (n < 3):
        return(fib[n])

    if (n > 2):
        while(n+1 != i ):
                fib.append( fib[i-1] + fib[i-2] )
                i=i+1


    return(fib[n])

#n = int(input())
n=3
print(calc_fib(n))
