# Write a function to calculate area and perimeter of a rectangle.

def rectangle(a,b):
    area = a*b
    print(area)
    para = 2*(a+b)
    print(para)
num1,num2 = map(int,input().split())
rectangle(num1,num2)