import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text = 'I am learning NLP(Natural Language Processing)'
tokens = word_tokenize(sample_text)

unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)