n = 0
s = 0
m = None  

while True:
    x = int(input("Enter le natural number (or -1 for sequence termination): "))

    if x == -1:
        break

    n = n + 1
    s = s + x

    if n == 1:
        m = x
    else:
        if x < m:
            m = x

if n == 0:
    m = -1
    a = -1
else:
    a = s / n

print("n =", n)
print("s =", s)
print("m =", m)
print("a =", a)