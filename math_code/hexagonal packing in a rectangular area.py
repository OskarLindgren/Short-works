import math

# change these for input (i'm never making sys params for this)
#---
X = 480 # rectangle size x
Y = 300 # rectangle size y
R = 50 # circle radius
# ---
  
def square(x, y, r):
    return (x // (2*r)) * (y // (2*r))

def hexagonal(x, y, r):
    if x < 2*r or y < 2*r:
        return 0
    rows = int((y - 2*r) // (r * math.sqrt(3))) + 1
    n = int(x // (2*r))
    n_alt = n if x >= 2*r*n + r else n - 1
    return math.ceil(rows/2) * n + (rows//2) * n_alt

best = max(square(X, Y, R), hexagonal(X, Y, R), hexagonal(Y, X, R))
print(best)
