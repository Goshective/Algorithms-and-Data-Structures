import time

def main():
    def calc_fib(n):
        if n in cache: return cache[n]
        if 0 <= n <= 1: return n
        res = calc_fib(n - 1) + calc_fib(n - 2)
        cache[n] = res
        return res

    cache = {}
    t_start = time.perf_counter()
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
    if 0 <= n <= 45:
        with open('output.txt', 'w') as f:
            f.write(str(calc_fib(n)))
    else:
        print("Число не соответствует условию.")
    print("Время работы: %s секунд " % (time.perf_counter() - t_start))


with open('input.txt', 'w') as f:
    f.write('10')
main()
with open('output.txt', 'r') as f:
        print("TEST 1. VERDICT:", "OK" if f.readline().strip() == '55' else "WRONG")

with open('input.txt', 'w') as f:
    f.write('3')
main()
with open('output.txt', 'r') as f:
        print("TEST 2. VERDICT:", "OK" if f.readline().strip() == '2' else "WRONG")