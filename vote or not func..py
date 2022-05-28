# Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )

def vote(age):
    if age >= 18:
        return 'you can vote'
    else:
        return 'you r not able to can vote'
a = int(input("Enter your age :"))
out = vote(a)
print(out)