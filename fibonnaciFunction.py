# n = int(input("enter the number here"))

# def fibonacci(n):
 
#     if n== 0:
#         return 0

#     elif n == 1:
#        return [0,1]
    
#     else:
#         fibonacci[1] = [0,1]
#         for i in range (2,n+1):
#             fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

#             return fibonacci(n)
        
# result = fibonacci(n)
# print(result)

        
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return [0, 1][n]
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number: "))
result = fibonacci(n)
print(result)