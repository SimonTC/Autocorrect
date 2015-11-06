from __future__ import division
from asyncio import Queue
import math, collections
class CustomLanguageModel:

  def __init__(self, corpus):
    self.grams = 2
    #How many instances of each n-gram exists in the training data
    self.counts = []    
    for i in range(self.grams):
        self.counts.append(collections.defaultdict(lambda: 0))
   
    #In how many different [n+1]-gram types is this n-gram used as the continuation n-gram
    self.counts_end = []    
    for i in range(self.grams):
        self.counts_end.append(collections.defaultdict(lambda: 0))
    
    #In how many different [n+1]-gram types is this n-gram used as the first n-gram
    self.counts_start = []    
    for i in range(self.grams):
        self.counts_start.append(collections.defaultdict(lambda: 0)) 
 
    self.discount = 0.75
    self.train(corpus)
    
  def add_count(queue, gram_id):
      """
      Increase the counts for the n-gram modeled by the queue
      """
      key = ''
      for x in queue:
          key+= x + ' '
      
      count_dict = self.counts[gram_id]
      count_dict[key] = count_dict[key] + 1
      
      if count_dict[key] == 1 and gram_id > 0:
          #This specific n-gram hasn't been seen before
          

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
      token_queues = [Queue(maxsize=i + 1) for i in range(self.grams)]
      for datum in sentence.data:
        token = datum.word
        for i, queue in enumerate(token_queues):
            queue.put(word)
            if queue.full():
                
        tokens.append(datum.word)
        count = 0        
        key = ''
            
      print tokens
        
        
        
        
        
#        if token_before != '':
#            key = '%s %s' %(token_before, token)
#            self.bigramCounts[key] = self.bigramCounts[key] + 1
#            if self.bigramCounts[key] == 1 :
#                self.continuationCounts_start[token_before] = self.continuationCounts_start[token_before] + 1                
#                self.continuationCounts_end[token] = self.continuationCounts_end[token] + 1
#        self.unigramCounts[token] = self.unigramCounts[token] + 1
#        self.total += 1        
#        token_before = token
#    self.bigram_types = len(self.bigramCounts)

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

