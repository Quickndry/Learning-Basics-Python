def digital_root(n):
    if len(str(n)) > 1:
        components = list(str(n))
        digits = [int(x) for x in components]
        sum_digits = sum(digits)
        if len(str(sum_digits)) > 1:
            sum_digits_recursion = digital_root(sum_digits)
            return(sum_digits_recursion)
        else:
            return(sum_digits)
    else:
        return(n)