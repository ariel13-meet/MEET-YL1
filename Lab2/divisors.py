n = int(raw_input())
def divisors(n):	
	for nu in range(n):			
		nu=nu+1
		if n%nu==0:
			print nu


divisors(n)
