# largest palendrome that is a product of 2x 3 digit numbers

lpal = 0
facs = []

def is_a_pal(n):
   return str(n)[::-1] == str(n)

for i in xrange(100,999):
   for j in xrange(100,999):
      k = i * j
      if is_a_pal(k) and k > lpal:
         facs = [i,j]
         lpal = k

print facs
print lpal
   


