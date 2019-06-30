# 4.1.3.10 LAB: Converting fuel consumption
# A car's fuel consumption may be expressed in many different ways. 
# For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
# In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.
# Your task is to write a pair of functions converting l/100km into mpg, and vice versa.
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres.

def l100kmtompg(liters):
    miles = (1/liters)* 100* 3.785411784/1.609344
    return miles


def mpgtol100km(miles):
    liters = (1/miles) * 100* 3.785411784/1.609344
    return liters

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))


testl100kmtompg = [3.9, 7.5, 10.]
testl100kmtompg_results = [60.31143162393162, 31.36194444444444, 23.52145833333333]
testmpgtol100km = [60.3, 31.4, 23.5]
testmpgtol100km_results = [3.9007393587617467, 7.490910297239916, 10.009131205673757]
for i in range(len(testl100kmtompg)):
	t = testl100kmtompg[i]
	print(t, "->", end="")
	result = l100kmtompg(t)
	if round(result,13) == round(testl100kmtompg_results[i],13):
		print("OK: ", result)
	else:
		print("Failed: ",result)

for i in range(len(testmpgtol100km)):
	t = testmpgtol100km[i]
	print(t, "->", end="")
	result = l100kmtompg(t)
	if round(result,13) == round(testmpgtol100km_results[i],13):
		print("OK: ", result)
	else:
		print("Failed: ",result)