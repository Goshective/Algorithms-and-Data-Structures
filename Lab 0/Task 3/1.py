import sys
import time

t_start = time.perf_counter()

def calc_fib(n):
    if 0 <= n <= 1: return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, (a + b) % 10
    return b

def main():
    t_start = time.perf_counter()
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
    if 0 <= n <= 10**7:
        res = calc_fib(n)
        with open('output.txt', 'w') as f:
            f.write(str(res))
    else:
        print("Число не соответствует условию.")
    print("Время работы: %s секунд " % (time.perf_counter() - t_start))


with open('input.txt', 'w') as f:
    f.write('331')
main()
with open('output.txt', 'r') as f:
    print("TEST 1. VERDICT:", "OK" if f.readline().strip() == '9' else "WRONG")

with open('input.txt', 'w') as f:
    f.write('327305')
main()
with open('output.txt', 'r') as f:
    print("TEST 2. VERDICT:", "OK" if f.readline().strip() == '5' else "WRONG")

with open('input.txt', 'w') as f:
    f.write('10000000')
main()
with open('output.txt', 'r') as f:
    print("TEST 3. VERDICT:", "OK" if f.readline().strip() == '5' else "WRONG")