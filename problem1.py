sum = 0
for i in tuple(range(1,1000)):
   if i % 3 == 0 or i % 5 == 0:
      sum += i
print sum
