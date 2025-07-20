

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

sample_text = 'I love programming in Python.'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)