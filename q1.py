'''Create a text content analyzer. This is a tool used by writers to
find statistics such as word and sentence count on essays or 
articles they are writing.

Write a Python program that analyzes input from a file and 
compiles statistics on it.

The program should output:

1. The total word count

2. The count of unique words

3. The number of sentences

Example output:


Total word count: 468
Unique words: 223
Sentences: 38

Brownie points will be awarded for the following extras:

1. The ability to calculate the average sentence length in words

2. The ability to find often used phrases (a phrase of 3 or more words 
used over 3 times)

3. A list of words used, in order of descending frequency
t
4. The ability to accept input from STDIN, or from a file specified 
on the command line.

This question should be written in Python. '''

import sys
import re
import pandas as pd
# from nltk import ngrams, FreqDist
# file = open('sample.txt', 'r')


def word_count(file):
	words = []
	reg_ex = r"[A-Za-z0-9']+"
	p = re.compile(reg_ex)
	for l in file:
		for i in p.findall(l):
			words.append(i)
	return len(words), len(set(words)), words

def sentence_count(file):
	sentences = []
	reg_ex = r"[a-zA-Z0-9)\"\]%\',\s]+[.!?]+"
	p = re.compile(reg_ex)
	for l in file: 
		for i in p.findall(l):
			sentences.append(i)
	return sentences, len(sentences)

def average_sentence_length(sentences):
	number_of_words = []
	counter = 0
	reg_ex = r"\s"
	p = re.compile(reg_ex)
	for i in sentences:
		sentence = p.split(i)
		for i in sentence:
			if i == '':
				pass
			else:
				counter += 1
		number_of_words.append(counter)
		counter = 0
	return float(sum(number_of_words)/len(sentences))

# def common_phrase(sentences):
# 	all_counts = dict()
# 	for i in sentences:
# 		for size in 3, 4, 5:
# 			all_counts[size] = FreqDist(ngrams(i, size))
# 	return all_counts

def list_of_words(unique_words, sentences):
	words = []
	dictionary = {}
	sorted_words = []
	reg_ex = r"[\s\.\?!]"
	p = re.compile(reg_ex)
	for s in sentences:
		for i in p.split(s):
			words.append(i)
	for u in unique_words:
		dictionary[u] = 0
	for w in words:
		if w in dictionary:
			dictionary[w] += 1
	sorted_by_value= sorted(dictionary.items(), key= lambda kv: kv[1], reverse = True)
	for i in sorted_by_value:
		sorted_words.append(i[0])
	return sorted_words


filename = sys.argv[1]

with open(filename, 'r') as f:
	sentences, sentence_count = sentence_count(f)
with open(filename, 'r') as f:
	word_count, unique_word_count, words = word_count(f)

print('Total word count:  {}\n'.format(word_count) + 
	'Unique words:  {}\n'.format(unique_word_count) + 
'Sentences:  {}\n'.format(sentence_count) +
'Average sentence length:  {}\n'.format(average_sentence_length(sentences)) + 
"List of common words from most to least frequent:  {}\n".format(list_of_words(set(words), sentences)))


