import mystuff

Mystuff = {'apple': "I AM APPLES!"}
print(Mystuff['apple'])

mystuff.apple()
print(mystuff.tangerine)

class MyStuff(object):
	def __init__(self):
		self.tangerine = 'My dream is to be happy and kickin!'

	def apple(self):
		print('This apple has a class!')


thing = MyStuff()
thing.apple()
print(thing.tangerine)

print(type(MyStuff))
print()


class Song(object):

	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_the_song(self):
		for words in self.lyrics:
			print(words)

hbday =[ 
"Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"
]
song_one = Song(hbday)

song_one.sing_the_song()