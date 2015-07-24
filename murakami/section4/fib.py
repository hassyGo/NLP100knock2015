def fib(n):
    if n < 2:
        return 1
    else:
        x = fib(n - 1)
        y = fib(n - 2)
        return x + y

print "aaaaa"