import re
import nltk
import gensim
from nltk.corpus import wordnet
from nltk.metrics import edit_distance
from nltk.corpus.reader.wordnet import WordNetCorpusReader
from gensim.models import Word2Vec
model = gensim.models.KeyedVectors.load_word2vec_format('C:\\Users\Daga\Desktop\GoogleNews-vectors-negative300.bin', binary=True)  

replacement_patterns = [
	(r'won\'t', 'will not'),
	(r'can\'t', 'cannot'),
	(r'i\'m', 'i am'),
	(r'ain\'t', 'is not'),
	(r'(\w+)\'ll', '\g<1> will'),
	(r'(\w+)n\'t', '\g<1> not'),
	(r'(\w+)\'ve', '\g<1> have'),
	(r'(\w+)\'s', '\g<1> is'),
	(r'(\w+)\'re', '\g<1> are'),
	(r'(\w+)\'d', '\g<1> would'),
]

patterns = [(re.compile(regex), repl) for (regex, repl) in replacement_patterns]
def replaceregex(text):
    s = text
    for (pattern, repl) in patterns:
        s = re.sub(pattern, repl, s)
    return s

repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
repl = r'\1\2\3'

def replacecharacters(word):
    if wordnet.synsets(word):
        return word
    repl_word = repeat_regexp.sub(repl, word)
    if repl_word != word:
        return replace(repl_word)
    else:
        return repl_word
    
def replace(word):
    antonyms = set()
    ans=None
    k=0.0
    m = wordnet.synsets(word)
    if(len(m)>0):
        final_syn = m[0]
    else :
        return ans
    for syn in m :
        r = syn.name().rsplit('.', 2)[1]
        if(r == 'a'):
            final_syn=syn
            break
    m1=""
    #print(final_syn.name().rsplit('.',2)[0])
    if word != final_syn.name().rsplit('.',2)[0]:
        return ans
    for lemma in syn.lemmas():
        for antonym in lemma.antonyms():
            antonyms.add(antonym.name())
            m1=antonym
            m1=m1.synset()
            final_syn_name = final_syn.name().rsplit('.', 2)[0]
            m1_name = m1.name().rsplit('.', 2)[0]
            if model.similarity(final_syn_name,m1_name) > k:
                k=model.similarity(final_syn_name,m1_name)
                ans=m1_name
    return ans
def replace_negations(sent):
    words = []
    i=0
    while i < len(sent):
        word = sent[i]
        if word == 'not' and i+1 < len(sent):
            print("replacing "+sent[i+1])
            ant = replace(sent[i+1])
            if ant:
                words.append(ant)
                i += 2
                continue
        words.append(word)
        i += 1
    return words

texts = [ " The Kabab wasn't good " , " The service was not good but the ambience was great " ]
for text in texts: 
	texts=nltk.sent_tokenize(text)
	for t in texts:
		t=replaceregex(t)
		words=nltk.word_tokenize(t)
		print(words)
		words=replace_negations(words)
		print(str(words))
