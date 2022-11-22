def nth_fib(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f_digit = 1
        s_digit = 1
        p_digit = 0

        for i in range(n-3):
            p_digit = f_digit
            f_digit = s_digit + f_digit
            s_digit = p_digit

        return f_digit