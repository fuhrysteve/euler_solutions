l = [2,1]
i = 0
j = 2
while i <= 4000000:
   i = sum(l)
   l.insert(0, i)
   l.pop()
   if i % 2 == 0:
      j += i
print j
  
