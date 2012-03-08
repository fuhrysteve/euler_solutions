# largest prime factor of the number 600851475143
n = 600851475143

def largest_prime(n):
   d = 2
   while d * d <= n:
      if n % d == 0:
         n /= d
      d=d+1
   return n

print largest_prime(n)
