from textblob import TextBlob
with open('dic.txt') as in_file,open('rat.csv','w') as out:
	s = ""
	n = 0
	x = 0.0
	for row in in_file:
		row = row[:-1]
		if s == "":
			s = row
		elif row[0] == 'e' and row[1] == 'n' and row[2] == 'd' and len(row) == 3:
			#print(x,n)
			x /= n
			se = s + "," + str(x)
			print(se)
			out.write(se)
			out.write("\n")
			n = 0
			x = 0.0
			s = ""
		else:
			a = row.split(',')
			test = TextBlob(a[0])
			#print(a[0] + " " + a[1] + " " + str(test.sentiment.polarity))
			x += float(test.sentiment.polarity)*(int(a[1]))
			n = n + int(a[1])