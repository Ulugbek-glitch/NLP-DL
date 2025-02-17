# -*- coding: utf-8 -*-
"""NLP

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UKyYPPgjcX1shOJYn8a3zUnoEkUJRdrt

# Stemming
"""

import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt_tab')

stemmer = PorterStemmer()
text = 'running runners ran easily'
tokens = nltk.word_tokenize(text)
stems = [stemmer.stem(token) for token in tokens]
print('Original Text: ', text)
print('Stemmed Test: ', stems)

"""# Lemmatization"""

from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token) for token in tokens]
print('Lemmatized Text: ', lemmas)

"""# POS Tags"""

nltk.download('averaged_perceptron_tagger_eng')

pos_tags = nltk.pos_tag(tokens)
print("POS Tags: ", pos_tags)

"""# Lemmatization and POS Tags with Spacy"""

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
lemmas = [token.lemma_ for token in doc]
pos_tags = [(token.text, token.pos_) for token in doc]
print('Lemmatized Text: ', lemmas)
print('POS Tags:', pos_tags)

"""# Advanced features"""

morphs = [token.morph for token in doc]
for token in doc:
  print(f'Token: {token.text}, Morph: {token.morph}')

"""# TextBlob"""

from textblob import TextBlob

blob = TextBlob(text)
words = blob.words
lemmas = [word.lemmatize() for word in words]
pos_tags = blob.tags
print('Words:', words)
print('Lemmatized Text:', lemmas)
print('POS Tags:', pos_tags)

"""# Syntax with NLTK"""

import matplotlib
matplotlib.use('Agg') # Use the Agg backend
from IPython.display import SVG, display
from nltk import pos_tag
from nltk.corpus import treebank
from nltk.tokenize import word_tokenize
from nltk.chunk import RegexpParser
#from nltk.draw.util import CanvasFrame # This line is causing the issue
#from nltk.draw import TreeWidget # This line depends on CanvasFrame, so we'll replace it
from nltk.tree import Tree # Import Tree for drawing
import svgling # Import the svgling package

sentence = "The quick brown fox jumps over the lazy dog"

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)
grammar = r""" NP:{<DT|JJ|NN.*>+}
PP:{<IN><NP>}
VP:{<VB.*><NP|PP|CLAUSE>+$}
CLAUSE:{<NP><VP>}   """

chunk_parser = RegexpParser(grammar)
parsed_tree=chunk_parser.parse(pos_tags)

tree = Tree.fromstring(str(parsed_tree)) # Convert the parsed tree to an nltk.tree.Tree object
svg_data = tree._repr_svg_() # Generate SVG data from the tree

display(SVG(svg_data)) # Display the SVG data

"""# Semantic Analysis"""

import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

synonyms = []
for syn in wordnet.synsets('happy'):
  for lemma in syn.lemmas():
    synonyms.append(lemma.name())
print(set(synonyms))

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import numpy as np
nltk.download('punkt_tab')

text = 'This is a sample sentence for demonstrating distributional semantics.Distributional semantics is based on the distributional hypothesis.'
token = word_tokenize(text)
print(token)

from nltk.corpus import wordnet
dog = wordnet.synset('dog.n.01')
cat = wordnet.synset('cat.n.01')
similarity = dog.wup_similarity(cat)
print(similarity)

"""# Lexi Semantic Analysis"""

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
text = 'Tokenizatsiya - bu matnni so\'zlarga va tinish belgilarga bo\'lish jarayoni'
tokens = nltk.word_tokenize(text)
tokens

normalized_tokens = [token.lower() for token in tokens if token.isalnum()]
normalized_tokens

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in normalized_tokens]
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in normalized_tokens]
pos_tags = nltk.pos_tag(normalized_tokens)
print(pos_tags)

from nltk import word_tokenize, pos_tag, ne_chunk
nltk.download('words')
text = 'Albert Einstein was born in Ulm, Germany in 1879.'

tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
ner_tags = ne_chunk(pos_tags)
print(ner_tags)