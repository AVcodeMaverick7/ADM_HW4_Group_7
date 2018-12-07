import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import ItalianStemmer
from nltk.tokenize import word_tokenize, regexp_tokenize
from collections import defaultdict
import numpy as np

def preprocess(text):
    text = text.lower()
    # removing '\n'
    text = text.replace('\\n', ' ')
    # removing punctuation
    tokenizer = regexp_tokenize(text, "[\w\$]+")
    # removing numbers
    filtered = [w for w in tokenizer if not w.isnumeric()]
    # filter the non stopwords
    filtered = [w for w in filtered if not w in stopwords.words('italian')]
    its = ItalianStemmer()
    # removing the stem
    filtered = [its.stem(word) for word in filtered]
    return filtered

# PREPROCESSING AND CREATING VOCABULARY FILE
vocabulary_set = set()
annouc_list = []
occurence_words_list = []

# open file with our data
with open("flat_data.txt", "r" ,encoding="utf-8") as flat_data:
    reader = csv.reader(flat_data, delimiter=",")
    for i, line in enumerate(reader):
        #if i%100==0: print(i) #to see the progress of calculations
        if line != [] and i!=0:
            # preprocess the dictionary text
            description = preprocess(line[5])
            # put new words to vocabulary set
            vocabulary_set.update(description)
            # put prepared words into the list with all announcements
            annouc_list.append(set(description))
            # count words frequency
            freq_word_dict = {}
            for w in description:
                try: freq_word_dict[w] += 1
                except: freq_word_dict[w] = 1
            # save the frequency dict for words in description
            occurence_words_list.append(freq_word_dict)
