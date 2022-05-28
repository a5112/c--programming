# Write a function to check if a number is even or not.

def even(n):
    if n %2==0:
        return 'even'
    else:
        return 'odd'
a = int(input())
print(even(a))