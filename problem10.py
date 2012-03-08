i = 2
pri = [i]
i += 1
pri.append(i)
while i < 2000000:
   i += 2
   tst = True
   for j in pri:
      if i % j == 0:
         tst = False
	 break
   if tst:
      pri.append(i)
      #print i
print sum(pri)
