import spacy
nlp = spacy.load('en_core_web_sm')
with open("a.txt","r") as f,open("out.txt","w") as out:
    for p in f:
        print(p)
        doc = nlp(p)
        noun_adj_pairs = []
        to = 0
        i = 0
        while to == 0 and i < len(doc):
            #print(i,doc[i])
            srt = ""
            if doc[i].pos_ not in ('NOUN','PROPN'):
                i = i +1
                continue
            else:
                srt+=str(doc[i])
                if  doc[i+1].pos_ in ('NOUN','PROPN'):   
                    while doc[i+1].pos_ in ('NOUN','PROPN'):
                        srt+=" "
                        srt+=str(doc[i+1])
                        i = i + 1
                        if i == len(doc)-1:
                            to = 1
                            break    
            for j in range(i+1,len(doc)):
                if doc[j].pos_ == 'ADJ': 
                    se = srt + "," + str(doc[j])
                    noun_adj_pairs.append(se)
                    break
            srt = ""
            if i == len(doc)-1:
                break
            #print(i)
            i = i +1
        for i,token in enumerate(doc):
            srt = ""
            if token.pos_ not in ('ADJ'):
                continue
            if i+1 < len(doc) and doc[i+1].pos_ in ('NOUN','PROPN'):
                while doc[i+1].pos_ in ('NOUN','PROPN'):
                    srt+=" "
                    srt+=str(doc[i+1])
                    i = i + 1     
                #i = i -1
                se = str(doc[i+1]) + "," + str(token)
                noun_adj_pairs.append(se)
                srt=""
        for pair in noun_adj_pairs :
            out.write(str(pair))
            out.write("\n")
            print(str(pair))
        print(" --------- " )