n = int(input("Enter a natural number n (>= 0): "))

# Set k = 0
k = 0

# Loop: check if the next square still fits
while (k + 1) * (k + 1) <= n:
    k = k + 1

# Set q = k * k
q = k * k
# Output q
print("The largest square number <= n is:", f"{k}^2 =", q)