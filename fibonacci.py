# for i in range(0,80):
#   print(i)
#   if i==3:
#     break
  

# for i in range (4):
#   print('printing')
#   if i==2:
#    continue  
#   print(i)  

n = int(input("Enter the number here"))

a = 0
b = 1
print(a,b, sep="\n")

for i in range(0,n-2):
    c = b
    b = b + a
    a = c
    print(b)

# print(b)
    
    