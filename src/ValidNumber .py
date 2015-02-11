def isNumber(s):
	try:
		float(s)
	except ValueError:
		return False
	else:
		return True

print isNumber("3")
print isNumber("0")
print isNumber(" 0.1 ")
print isNumber("abc")
print isNumber("1 a")
print isNumber("2e10")

# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true

	