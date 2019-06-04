import spacy
nlp = spacy.load('en_core_web_sm')
with open("group2_taste.txt","r") as f,open("out.txt","w") as out:
	for p in f:
		out.write(p)
		doc = nlp(p)
	noun_adj_pairs = []
	for i in range(0,len(doc)):
		s=""
		if doc[i].pos_ not in ('NOUN','PROPN'):
			continue
		else:
			ip = i
			if doc[i].pos_ in ('NOUN','PROPN'):
				while(doc[i].pos_ in ('NOUN','PROPN')):
					s+=str(doc[i])
					i+=1
			i = ip
		for j in range(i+1,len(doc)):
			if doc[j].pos_ == 'ADJ':
				noun_adj_pairs.append((s,doc[j]))
				break
	for i in range(0,len(doc)):
		s=""
		if doc[i].pos_ not in ('ADJ'):
			continue
		if doc[i+1].pos_ in ('NOUN','PROPN'):
			ip = i
			while(doc[i+1].pos_ in ('NOUN','PROPN')):
				s+=str(doc[i+1])
				i+=1
			i= ip
			noun_adj_pairs.append((s,doc[i]))
	#for pair in noun_adj_pairs:
	print(len(noun_adj_pairs))
	for i,j in noun_adj_pairs:
		s=str(i)+","+str(j)
		out.write(s)
		print(s)
		out.write("\n")
#	out.write(str(noun_adj_pairs))
#	out.write("\n")