# Number system conversion calculator

decimal_no = int(input("Enter the decimal number :"))
base = int(input("Enter 8 for octal,2 for binary, 16 for hexadecimal :"))

def binary():
	global decimal_no
	global base
	a = []
	for i in range(100**100):
		binary = decimal_no % 2
		a.append(binary)
		decimal_no = decimal_no//2
		if decimal_no == 0:                                                                                                                                                                                                                                                                                                             
			break
		#a.append(binary)
		#print(decimal_no," ",binary)
	#a.append(1)
	print(a)		
def octal():
	global decimal_no
	global base
	b = []
	for i in range(100**100):
		octal = decimal_no % 8
		b.append(octal)
		decimal_no = decimal_no//8
		if decimal_no == 0:
			break
		#print(decimal_no," ",octal)
	b.reverse()
	print(b)

def hexa():
	global decimal_no
	global base
	c = []
	for i in range(100**100):
		hexa = decimal_no % 16
		c.append(hexa)
		decimal_no = decimal_no//16
		if decimal_no == 0:
			break
		#print(decimal_no," ",hexa)
	c.reverse()
	for numbers in c:
		if numbers == 10:
			index = c.index(numbers)
			c.pop(index)
			c.insert(index,"A")
		
		if numbers == 11:
			index = c.index(numbers)
			c.pop(index)
			c.insert(index,"B")
			
		if numbers == 12:
			index = c.index(numbers)
			c.pop(index)
			c.insert(index,"C")
			
		if numbers == 13:
			index = c.index(numbers)
			c.pop(index)
			c.insert(index,"D")
			
		if numbers == 14:
			index = c.index(numbers)
			c.pop(index)
			c.insert(index,"E")
			
		if numbers == 10:
			index = c.index(numbers)
			c.pop(index)
			c.insert(index,"F")
			
	print(c)
	
if base == 2:
	binary()
elif base == 8:
	octal()
else:
	hexa()	
							
