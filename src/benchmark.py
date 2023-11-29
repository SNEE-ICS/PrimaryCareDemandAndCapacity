from time import perf_counter


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    start = perf_counter()
    FIB_N = 40
    fibonacci(FIB_N)
    end = perf_counter()
    print(f'Recursive fibonacci of n = {FIB_N} Execution time (seconds): {end - start}')