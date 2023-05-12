#Importing the Module:
import opening_file

#Defining a file path:
file_path = 'D:/Python_work/text_files/All_Words.txt'

#loading the List of word:
load_list = opening_file.open_file(file_path)

#Function to get a word from the List:
def find_palindromes(word_list):
	'''Finding palindromes'''
	for word in word_list:
	    if word[:] == word[: :-1]:
	    	palindromes.append(word)

#Creating an empty list to store palindromes:
palindromes = []

#Calling the function:
find_palindromes(load_list)

