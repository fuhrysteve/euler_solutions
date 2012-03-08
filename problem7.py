
i = 2
pri = [i]
i += 1
pri.append(i)
while len(pri) < 10001:
   i += 2
   tst = True
   for j in pri:
      if i % j == 0:
         tst = False
   if tst:
      pri.append(i)
      #print i
print pri[-1]
