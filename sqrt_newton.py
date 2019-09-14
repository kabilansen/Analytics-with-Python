#Write a function squareRoot(x) to compute the square root of the positive number by newton-raphson method.
def squareRoot(x, a):
    for i in range(3):
        x = x -  (((x**2) - (a))/(2*x))
        print(x)
x = 2
a = 5


#Write a function myPi(n) to compute pi by Gregory series.
def piGreg(n):
    sum = 0
    for i in range(1, n):
        sum = sum+((-1)**(i+1)/((2*i)-1))
    print(4*sum)
squareRoot(x,a)
print("Pi:\n")
piGreg(10000)