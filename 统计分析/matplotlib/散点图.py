import matplotlib.pyplot as plt


x1 = []
y1 = []

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))


def f_2(x,a,b,c):
    return a*(x**2)+b*x+c

x = -(b/(2*a))
x = float(x)
x1.append(x)
x1.append(x+1)
x1.append(x+2)
x1.append(x-1)
x1.append(x-2)

ya = f_2(x,a,b,c)
y1.append(ya)
yb = f_2(x+1,a,b,c)
y1.append(yb)
yc = f_2(x+2,a,b,c)
y1.append(yc)
yd = f_2(x-1,a,b,c)
y1.append(yd)
ye = f_2(x-2,a,b,c)
y1.append(ye)

plt.scatter(x1,y1,s=10,c='b')
plt.xlabel('x x')
plt.ylabel('y y')

plt.show()

