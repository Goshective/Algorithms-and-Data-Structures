import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.utils import read_len_double_lst_file, write_lst_file


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
    n, a, b = read_len_double_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), int)
    res = multiply_polynoms(n, a[::-1], b[::-1])
    if res[-1] == 0:
        res.pop()
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), res[::-1])


if __name__ == "__main__":
    main()