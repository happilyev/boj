import sys
input = sys.stdin.readline

mod = 1000000000

def mat_mul(a, b):
    return [[(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod,
             (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod,
             (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]]

def mat_pow(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half = mat_pow(matrix, n//2)
        return mat_mul(half, half)
    else:
        return mat_mul(matrix, mat_pow(matrix, n-1))
def fib(n):
    if n == 0:
        return 0
    else:
        base = [[1,1],[1,0]]
        result = mat_pow(base, n)
        return result[0][1]

n, k = map(int, input().split())

    
print((fib(b+2) - fib(a+1))% mod)