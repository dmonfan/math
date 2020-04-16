import math
sum = 0
i = 1
n = 1
while(n < 100):
	while(i <= n):
		sum += (math.pi/n)*math.sin(math.pi/n*i)
		i += 1
	print(sum)
	i = 1
	sum = 0
	n += 1