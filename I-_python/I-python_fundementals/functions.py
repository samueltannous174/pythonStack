
print("CODE 1:")
def a():
    return 5
print(a())

print("\nCODE 2:")
def a():
    return 5
print(a()+a())

print("\nCODE 3:")
def a():
    return 5
    return 10
print(a())

print("\nCODE 4:")
def a():
    return 5
    print(10)
print(a())

print("\nCODE 5:")
def a():
    print(5)
x = a()
print(x)

print("\nCODE 6:")
def a(b,c):
    return b+c
print(a(1,2) + a(2,3))

print("\nCODE 7:")
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

print("\nCODE 8:")
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

print("\nCODE 9:")
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

print("\nCODE 10:")
def a(b,c):
    return b+c
    return 10
print(a(3,5))

print("\nCODE 11:")
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

print("\nCODE 12:")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

print("\nCODE 13:")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

print("\nCODE 14:")
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

print("\nCODE 15:")
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

