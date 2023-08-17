n=int(input("Enter the number:"))
sum=0
while n>0:
    if n%2==1:
        sum+=n
    n-=1
print("Sum upto given no. is",sum)