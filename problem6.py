sum_sq = 0
sq_sum = 0

for i in xrange(1, 101):
   sum_sq += pow(i, 2)

for i in xrange(1, 101):
   sq_sum += i
sq_sum = pow(sq_sum, 2);

print sq_sum - sum_sq

