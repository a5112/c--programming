# Program to input two numbers and subtract the smaller number from the greater number.

num1,num2 = map(int,input().split())
if num1>num2:
    out= num1-num2
else:
    out=num2-num1
print(out)