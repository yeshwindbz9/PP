people = int(input('Enter the number of people ..\n'))
dogs = int(input('Enter the number of dogs ..\n'))
cats = int(input('Enter the number of cats ..\n'))

if people > dogs:
	print('Hey there are not enough dogs..')
	print('thats not cute')
else:
	print("Thats fine who gonna hug people when we've got dogs")
if people > cats:
	print('We dont need more cats ,Good job...')
else:
	print('we need more people not more cats...')
if cats > dogs:
	print('Ughh! i hate cats.')
else:
	print('Cats are sick , pups are cute')