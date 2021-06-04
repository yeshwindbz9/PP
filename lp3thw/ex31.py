print('''
You enter a dark room with two doors..
Choose door #1 or door #2
else press 3 or anything else if you wanna stay here!
''')
door = int(input('>'))

if door == 1:
	print('Theres a giant bear eating cake')
	print('What would you do? : ')
	print('\t1.Take the cake')
	print('\t2.Scream at the bear')
	print('\t3.Do nothing')

	ch = int(input('>>'))

	if ch==1:
		print('The bear eats you and the cake..')
	elif ch==2:
		print('The bear growls at you then eats you..')
	else:
		print('The bear gets sleepy')
		print('The bear goes away to sleep')

elif door == 2:
	print('You encounter the ghost rider')
	print('He tells you to look into his eyes and youll feel the pain')
	print('You see : ')
	print('\t1.blueberries')
	print('\t2.your girlfriend')
	print('\t3.The souls youve tortured and killed')

	look = int(input('>>'))

	if look== 1 or look == 2:
		print('You are not evil')
		print('The ghost rider gives you a ride home...')
	else:
		print('You are dead')
		print('Your soul goes to hell!')

else:
	print('A naked man comes and strikes you down')
	print('He steals your clothes')
	print('Now your naked and dead')