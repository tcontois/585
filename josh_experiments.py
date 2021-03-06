from collections import defaultdict
from textblob import TextBlob
import sequence
import random

def getwords():
	filew = open('datasets/dictionaryforalex.txt','w')
	file = open('datasets/short_fp.txt')
	text = file.read()
	t = TextBlob(text.decode('ascii', 'ignore'))
	#t = TextBlob(text)
	wordlist = t.tags
	taglist = {}
	#print wordlist
	for k,v in wordlist:
		filew.write(k+" "+v+'\n')
		if v in taglist:
			taglist[v].append(k)
		else:
			taglist[v] = [k]
	return taglist



def writeseq():
	filew = open('datasets/sequence.txt','w')
	file = open('datasets/obama_speeches.txt')
	text = file.read()
	t = TextBlob(text.decode('ascii','ignore'))
	#t = TextBlob("Hello. This is a sample text. I fuckin hate alex lSSALLE.! yes !")
	wordlist = t.tags
	taglist = {}
	for k,v in wordlist:
		filew.write(v+" ")


if __name__ == '__main__':
	writeseq()
	open_file=open('./datasets/sequence.txt')
	pos_dictionary=getwords()

	sequence_markov=sequence.Markov(open_file)
	pos_sequence= sequence_markov.generate_markov_text().split()
	sentence=''
	first=True
	for x in range(0,5):
		for tags in pos_sequence:
			if (first):
				sentence=pos_dictionary[tags][random.randint(0,len(pos_dictionary[tags])-1)]
				while not sentence[0].isupper():
					sentence=pos_dictionary[tags][random.randint(0,len(pos_dictionary[tags])-1)]
				first=False
			else:
				sentence=sentence+' '+ pos_dictionary[tags][random.randint(0,len(pos_dictionary[tags])-1)]
		print sentence
		print
		sentence=''

	getwords()

