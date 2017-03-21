def words(sentence):
	"""
	Counts the occurrences or characters in a word
	"""
	my_words = sentence.split()
	my_dict = {}

	for w in my_words:
		if w in my_dict:
			my_dict[w] += 1

		else:
			my_dict[w] = 1

	return(my_dict)

