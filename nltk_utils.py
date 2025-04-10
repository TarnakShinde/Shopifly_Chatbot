from nltk.tokenize import TreebankWordTokenizer
from nltk.stem.porter import PorterStemmer
import numpy as np

stemmer = PorterStemmer()
tokenizer = TreebankWordTokenizer()  # ✅ No 'punkt' required

def tokenize(sentence):
    return tokenizer.tokenize(sentence)  # ✅ Uses Treebank tokenizer

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag
