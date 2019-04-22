# Set maximum to the max value of any set of numbers on line 3!

maximum = max(12, 13, 14, 15, 16)
print(maximum)

# limit

mx = 10
mi = 1

for x in (1,22,3,42,5,-1,11,9,-10,10):
	print('limit ({}): {}'.format(x, max(min(x, mx), mi)))