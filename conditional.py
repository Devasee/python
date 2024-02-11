# if statement
print("Enter your 4 subject numbers here")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = (a + b + c + d) / 4

if x > 75:
    print('First')

elif x > 55:
    print('Second')

elif x > 40:
    print('Third')

else:
    print('Fail')
