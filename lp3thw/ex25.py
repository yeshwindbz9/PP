def break_words(stuff):
	'''this function will break sentences into words'''
	words = stuff.split(' ')
	return words

def sort_words(words):
	'''sorts the words..'''
	return sorted(words)

def print_first_word(word):
	'''prints the first word after poppint it off'''
	word = word.pop(0)
	print(word)

def print_last_word(word):
	'''prints the last word before popping it off'''
	word = word.pop(-1)
	print(word)

def sort_sentences(sentence):
	'''takes in a sentence and returns the sorted words'''
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentences):
	'''prints first and last words of a sentence'''
	words = break_words(sentences)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentences):
	'''prints first and last words of a sorted sentence'''
	words = sort_sentences(sentences)
	print_first_word(words)
	print_last_word(words)



