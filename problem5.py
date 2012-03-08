def primer():
   n = 1
   while True:
      w = True
      for i in xrange(1,20):
         if n % i != 0:
            w = False
	    break
      if w == True:
         return n
      n += 1
print primer()
