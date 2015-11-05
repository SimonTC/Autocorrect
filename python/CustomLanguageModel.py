from __future__ import division
import math, collections
class CustomLanguageModel:

  def __init__(self, corpus):
    #How many times does is this bigram seen in the training set
    self.bigramCounts = collections.defaultdict(lambda: 0)
    #How many times is this unigram seen in the training set
    self.unigramCounts = collections.defaultdict(lambda: 0)
    #In how many different bigram types is this word used as the continuation word
    self.continuationCounts_end = collections.defaultdict(lambda: 0)
    #In how many different bigram types is this word used as the first word
    self.continuationCounts_start = collections.defaultdict(lambda: 0)  
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
                self.continuationCounts_start[token_before] = self.continuationCounts_start[token_before] + 1                
                self.continuationCounts_end[token] = self.continuationCounts_end[token] + 1
        self.unigramCounts[token] = self.unigramCounts[token] + 1
        self.total += 1        
        token_before = token
    self.bigram_types = len(self.bigramCounts)

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0 
    token_before = ''
    for token in sentence:
      if token_before != '':
          key = '%s %s' %(token_before, token)
          count = self.bigramCounts[key] - self.discount + 1
          count_before = self.unigramCounts[token_before] + self.bigram_types
          prob_bigram = count / count_before 
          prob_cont = self.continuationCounts_end[token] / self.bigram_types
          weight = (self.discount / count_before) * self.continuationCounts_start[token_before]
          prob = prob_bigram + weight * prob_cont
          if prob > 0:
              score += math.log(prob)
      token_before = token
    return score

