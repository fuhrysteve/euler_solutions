
def trip(n):
   for i in xrange(1,999):
      for j in xrange(1,999):
         for k in xrange(1,999):
            if i+j+k == 1000 and pow(i,2) + pow(j, 2) == pow(k, 2):
               print "%d^2 + %d^2 + %d^2" % (i,j,k)
	       print "product, abc = %d" % (i*j*k)
	       return
trip(1000)
