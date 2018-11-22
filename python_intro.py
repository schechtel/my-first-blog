#DjangoGirls

#print('Hello, DjangoGirls!')

#if 3>2:
#	print('It works!')

#volume = 57
#if volume <20:
#	print('it\'s kinda quiet')
#elif 20 <= volume < 40:
#	print('it\'s nice for background music')
#elif 40 <= volume < 60:
#	print('Perfect, I can hear all the details')
#elif 60 <= volume < 80:
#	print('nice for parties')
#elif 80 <= volume < 100:
#	print ('a bit loud!')
#else:
#	print('MY EARS ARE HURTING :(')

#def hi():
#	print('hi there!')
#	print('how are you?')

#def hi(name):
#	if name == 'Ola':
#		print('Hi Ola!')
#	elif name == 'Tahiel':
#		print('Hi Tahiel!')
#	else:
#		print('Hi annonymous')
#name='Tahiel'
#hi(name)
#hi('Kat')

def hi(name):
	print('Hi '+ name + '!')

girls = ['Luisa', 'Mica', 'Tahiel', 'Marilyn']

for name in girls:
	hi(name)
	print('Next!')