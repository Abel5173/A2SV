def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)

def lcm(a,b):
	return (a // gcd(a,b))* b

ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
a = abs(ds - ys)
b = abs(dm - ym)
print(lcm(a,b))