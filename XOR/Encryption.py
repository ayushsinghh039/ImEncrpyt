
try:
	# take path of image
	path = input(r'Enter path of Image : ')
	
#encrypton key
	key = int(input('Enter Key for encryption of Image : '))
	print('The path of file : ', path)
	print('Key for encryption : ', key)
	fin = open(path, 'rb')
	

	image = fin.read()
	fin.close()
	
	# converting image into byte array 
	image = bytearray(image)

	#xor in bytearray
	for index, values in enumerate(image):
		image[index] = values ^ key


	fin = open(path, 'wb')
	
	
	fin.write(image)
	fin.close()
	print('Encryption Done...')

	
except Exception:
	print('Error caught : ', Exception.__name__)
