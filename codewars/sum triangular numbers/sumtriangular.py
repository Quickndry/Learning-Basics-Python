# Works
def sum_triangular_numbers(n):
    placeholder = 0
    target = 0
    for i in range(n+1):
        placeholder += i
        target += placeholder
    return target