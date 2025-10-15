def z_index(N, r, c):
    index = 0
    size = 2 ** N
    while size > 1:
        half = size // 2
        row = 1 if r >= half else 0
        col = 1 if c >= half else 0
        quadrant = row * 2 + col
        index += quadrant * (half * half)
        if row == 1:
            r -= half
        if col == 1:
            c -= half
        size = half
    return index

N, r, c = map(int,input().split())
print(z_index(N,r,c))
