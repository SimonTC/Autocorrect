import math, collections

class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    self.bigramCounts = collections.defaultdict(lambda: 0)
    self.unigramCounts = collections.defaultdict(lambda: 0)
    self.total = 0    
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
            self.total += 1
        self.unigramCounts[token] = self.unigramCounts[token] + 1
        token_before = token

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0 
    token_before = ''
    for token in sentence:
      if token_before != '':
          key = '%s %s' %(token_before, token)
          count = self.bigramCounts[key]
          count_uni = self.unigramCounts[token_before]
          score += math.log(count + 1) #Smoothing by adding 1
          score -= math.log(count_uni + self.total) #Smoothing by adding the vocabulary
      token_before = token
    return score
