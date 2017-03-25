def string_length(strings):
	""" 
	return the length of the string/strings in a list
	"""
	my_list = []

	if strings == str(strings):
		length = len(strings)
		my_list.append(length)

	else:
		for i in strings:
			length = len(i)
			my_list.append(length)

	return(my_list)
