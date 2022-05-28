'''Program to display the table of an entered number in the following format:
2*1=2
2*2=4
...........
2*10=20'''

num = int(input())
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
