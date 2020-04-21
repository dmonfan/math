from math import pi, sin
sum = 0
i = 1
n = 2
while(n < 100):
	while(i <= n):
		sum += (pi/n)*sin(pi/n*i)
		i += 1
	print(sum)
	i = 1
	sum = 0
	n += 1
