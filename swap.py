x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: '+ str(x))
print('The value of y after swapping: '+ str(y))


x = input('Enter value of x: ')
y = input('Enter value of y: ')
x, y = y, x
print("x =", x)
print("y =", y)

x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x + y
y = x - y
x = x - y
print("x =",x)
print("y =", y)

x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x * y
y = x // y
x = x // y
print("x =",x)
print("y =", y)

x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x ^ y
y = x ^ y
x = x ^ y
print("x =",x)
print("y =", y)
