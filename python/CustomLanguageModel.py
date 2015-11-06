from __future__ import division
import math, collections
class CustomLanguageModel:

  def __init__(self, corpus):
    #How many times does is this bigram seen in the training set
    self.bigramCounts = collections.defaultdict(lambda: 0)
    #In how many different bigram types is this word used as the continuation word
    self.continuationCounts_end = collections.defaultdict(lambda: 0)
    self.total = 0    
    self.discount = 0.75
    self.train(corpus)
    

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
      token_before = ''
      for datum in sentence.data:
        token = datum.word
        if token_before != '':
            key = '%s %s' %(token_before, token)
            self.bigramCounts[key] = self.bigramCounts[key] + 1
            if self.bigramCounts[key] == 1 :
                self.continuationCounts_end[token] = self.continuationCounts_end[token] + 1
        self.total += 1        
        token_before = token
    self.bigram_types = len(self.bigramCounts)

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0 
    for token in sentence:
        count_continuation = self.continuationCounts_end[token]
        prob = count_continuation / self.bigram_types
        score *= prob
    return score

