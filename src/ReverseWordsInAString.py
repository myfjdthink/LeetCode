
def reverse(strs):
	
	#print anser
	print ' '.join(filter(lambda x: x != '' , list(reversed(strs.split(' ')))))
	#print filter(lambda x: x ==, strs.split(' '))
	#print ' '.join(list(reversed(strs.strip(' ').split(' '))))


reverse("the sky is blue")
reverse("the sky ")
reverse("a   b")
reverse(" ")


	