#합
def f(n):
    if n <= 1:
        return 1
    else:
        return n + f(n-1)

n = 100
print(f(n)) 


#곱
m = 5
def f(m):
    if m <= 1:
        return 1
    else:
        return m * f(m-1)
print(f(m))