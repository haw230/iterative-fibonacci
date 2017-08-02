def solved_fib(n):
    fn0 = 1
    fn1 = 1
    for i in range(n):
        temp = fn0
        fn0 = fn1
        fn1 += temp
    return fn0
