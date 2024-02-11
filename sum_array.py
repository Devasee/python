data = [2,45,65,76,78,89]

length = len(data)
sum = 0
for i in range(0, length):
  sum += data[i]

average = sum/length
print(average)