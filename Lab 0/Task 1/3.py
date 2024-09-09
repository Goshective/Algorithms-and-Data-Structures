with open('input.txt', 'r') as f:
    a, b = map(int, f.readline().strip().split())
with open('output.txt', 'w') as f:
    print(a + b, file=f)