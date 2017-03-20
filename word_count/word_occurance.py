def words(sentence):
	"""
        Counts the occurrences or characters in a word
    """
	my_dict = {}

	for w in sentence.split():
		my_dict[w] = sentence.count(w)

	return(my_dict)

