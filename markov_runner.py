from __future__ import division
import markov_text_gen
from collections import defaultdict

file_=open('obama_speeches.txt')
markov=markov_text_gen.Markov(file_)
print markov.generate_markov_text()