i=int(input())
x=2
while i>x:
    if i % x == 0:
        print(x)
        i /= x
    else:
        x += 1
print(int(i))

