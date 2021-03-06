import operator 
import json
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import bigrams 
from collections import Counter
import string
import re

import preprocessing
 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via',]



infile = 'tweets.json'
with open(infile, 'r') as f:
  terms_counter = Counter()
  bigrams_counter = Counter()

  for line in f:
    if len(line.strip()) > 0:
      tweet = json.loads(line)
      terms = [term for term in preprocessing.preprocess(tweet['text'], True) if term not in stop and re.search('[a-zA-Z]', term) and re.search('@', term) is None]
      # Update counters
      terms_counter.update(terms)
      bigrams_counter.update(bigrams(terms))

  print(terms_counter.most_common(5))
  print(bigrams_counter.most_common(5))