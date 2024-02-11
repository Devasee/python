sum = 0
# print("enter the even number here")

for x in range(10):
    n = int(input("enter the even number"))

    if n%2!=0:
       break
    sum = sum + n

print('Sum =' ,sum)