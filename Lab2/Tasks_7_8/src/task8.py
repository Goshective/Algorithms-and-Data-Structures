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

def sum_polynoms(A, B, shift_A=0, shift_B=0):
    len_r = max(len(A) + shift_A, len(B) + shift_B)
    R = [0] * len_r
    i = min(shift_A, shift_B)
    while i < len_r:
        if 0 <= i-shift_A < len(A):
            R[i] += A[i - shift_A]
        if 0 <= i-shift_B < len(B):
            R[i] += B[i - shift_B]
        i += 1
    return R

def multiply_polynoms(n, A, B):
    if n == 1:
        return [A[0] * B[0]]

    A0, A1 = A[:n//2], A[n//2:]
    B0, B1 = B[:n//2], B[n//2:]
    if len(A0) < len(A1):
        A0.append(0)
    if len(B0) < len(B1):
        B0.append(0)
    l = len(A0)
    U = multiply_polynoms(l, A0, B0)
    V = multiply_polynoms(l, A0, B1)
    W = multiply_polynoms(l, A1, B0)
    Z = multiply_polynoms(l, A1, B1)

    VW = sum_polynoms(V, W, n//2, n//2)
    UZ = sum_polynoms(U, Z, shift_B=2*(n//2))
    R = sum_polynoms(VW, UZ)
    return R

def main():
    with open('input.txt8', 'r') as inp, open('output.txt', 'w') as out:
        n = int(inp.readline())
        a = [int(x) for x in inp.readline().split()]
        b = [int(x) for x in inp.readline().split()]
        res = multiply_polynoms(n, a[::-1], b[::-1])
        if res[-1] == 0:
            res.pop()
        print(*res[::-1], file=out, end='')
    return

if __name__ == "__main__":
    main()