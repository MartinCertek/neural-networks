import random

res = "["
for i in xrange(2000):
    
	pohlavie = ['1,','0,']
	p=(random.choice(pohlavie))

	bydlisko = ['1,','0,']
	b=(random.choice(bydlisko))

	vek = ['0,0,0,0,1,', '0,0,0,1,0,', '0,0,1,0,0,', '0,1,0,0,0,', '1,0,0,0,0,']
	v=(random.choice(vek))

	roky = ['0,0,0,1,', '0,0,1,0,', '0,1,0,0,', '1,0,0,0,']
	r=(random.choice(roky))

	vzdelanie = ['1','0']
	vz=(random.choice(vzdelanie))

	prestup = ['1','0']
	pr=(random.choice(prestup))

	res= res+"(("+p+b+v+r+vz+"),"+pr+"), \n"

res = res[:-3]+"]"
print res

file = open("newfile.txt", "w")
file.write(res)
file.close()