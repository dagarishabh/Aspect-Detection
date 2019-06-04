import nltk
from nltk import RegexpParser
with open("out_group2_taste.txt","a") as f1:
    def func(document):
        #print(document)
        sentences = nltk.sent_tokenize(document)
        #print(sentences)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        #print(sentences)
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        #print(sentences)
        grammar = r'NP: {<JJR|JJS|JJ|NN|NNP|NP.*>+}'
        cp = RegexpParser(grammar)
        for sent in sentences:
            result = cp.parse(sent)
            #print(result)
            #result.draw()
            for subtree in result.subtrees():
                if subtree.label() == 'NP':
                    #print(subtree)
                    z=str(subtree)
                    z+='\n'
                    print(z)
                    f1.write(z)
    with open("group2_taste.txt","r") as f:
        ctr=1;
        while(1):
            p=f.readline()
            if(p):
                q=str(ctr)
                q+=". "
                q+=p
                print(q)
                f1.write(q)
                func(p)
                ctr+=1
            else:
                break;
