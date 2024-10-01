def multiply_polinoms(n, A, B, a_i, b_i):
    R = [0] * (2*n - 2)
    if n == 1:
        R[0] = A[a_i] * B[b_i]
        return R
    R[:n-2 + 1] = multiply_polinoms(n//2, A, B, a_i, b_i)
    R[n: 2*n-2] = multiply_polinoms(n//2, A, B, a_i + n//2, b_i + n//2)

    D0E1 = multiply_polinoms(n//2, A, B, a_i, b_i + n//2)
    D1E0 = multiply_polinoms(n//2, A, B, a_i + n//2, b_i)

    R[n//2:n+n//2 - 2 + 1] += D1E0 + D0E1
    return R

def main():
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        n = int(inp.readline())
        a = [int(x) for x in inp.readline().split()]
        b = [int(x) for x in inp.readline().split()]
        res = multiply_polinoms(n, a, b)
        print(*res, file=out, end='')