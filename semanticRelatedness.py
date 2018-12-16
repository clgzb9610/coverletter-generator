from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize


# bank_sents = ['I went to the bank to deposit my money',
# 'The river bank was full of dead fishes']
# ans = max_wupa(bank_sents[0], 'bank')
# print(ans)
# print(ans[0][1].definition)

hit = wn.synset('hit.v.01')
slap = wn.synset('slap.v.01')
print(wn.path_similarity(hit, slap))
print(wn.lch_similarity(hit, slap))
print(wn.wup_similarity(hit, slap))

print(wn.synsets('dog'))
# print(wn.synsets('development')[3].name())