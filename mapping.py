pre = set()
with open('a.txt','r') as in_file,open('out_file.txt','w') as out_file:
	nouns = list()
	adj = list()
	str = ""
	for row in in_file:
		if row[0]  == '(' :
			print(row)
			row = row[1:-1]
			row = row[:-1]
			arr = row.split(' ')
			#print(arr)
			nou = ""
			for a in arr:
				b = a.split('/')
				#print(b)
				if len(b)>1:
					if b[1] == 'NN' or b[1] == 'NP' or b[1] == 'NNP' or b[1] == 'NNS':
						nou = nou + b[0] + " "
					else :
						if nou != "":
							nou = nou[:-1]
							nouns.append(nou)
							nou = ""
						if b[1] == 'JJ' or b[1] == 'JJR' or b[1] == 'JJS' :
							adj.append(b[0])
			if nou != "":
				nou = nou[:-1]
				nouns.append(nou)
		else : 
			#out_file.write(str)	
			print(nouns)
			print(adj)
			for n in nouns:
				for a in adj:
					s = n + "," + a
					print(s)
					out_file.write(s)
					out_file.write("\n")
			#out_file.write("\n")
			nouns.clear()
			adj.clear()
			str = row
	#out_file.write(str)	
	print(nouns)
	print(adj)
	for n in nouns:
		for a in adj:
			s = n + "," + a
			print(s)
			out_file.write(s)
			out_file.write("\n")
	nouns.clear()
	adj.clear()
	str = row