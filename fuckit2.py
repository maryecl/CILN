dictionary = {}
t = "0"


#If this  word has already a type assigned, we increment the number of appearance of the word in that type
#If it's the first time that the word appears in a certain type, new type discovered = 1

class word(): #class word, where we work with the word structure, count its tag types, generate the lexic.txt and choose its most probable tag 
	
	def __init__(self):
		self.type_options = {}
		self.probable_type = ''
		self.tag_number = ''

	def count_types(self, type):
		if type in self.type_options:
			self.type_options[type]+=1
		else:
			self.type_options[type]=1
		

	def word_types(self, word): # Generazionne del modelooo  PAzzO 1 

		t = ''
		for type in self.type_options:
			t =  t+word+"\t"+type+"\t"+str(self.type_options[type])+"\n"	
		return t 
		

	def most_probable_type(self):
		self.temp_prob = ('',0)
		#types = count_types()
		if self.probable_type is '':
			for type in self.type_options:
				if self.type_options[type] > self.temp_prob[1]:
					self.temp_prob = (type, self.type_options[type])
			self.probable_type = self.temp_prob[0]
			return self.probable_type
	
		else:
			return self.probable_type
    
	def max_tag(self):
		self.temp_tag = ''
		for type in self.type_options:
			if self.tag_number<self.type_options[type]:
				self.temp_tag = self.type_options[type]
				self.tag_number = self.temp_tag
		return self.tag_number
	

def split_corpus(): #If word in dictionary, we analtyze its types, if not in dict, then we create and add this new word
	global dictionary
	l = ''
	f = open("corpus.txt")
	for line in f:
		line = line.decode("latin_1").encode("UTF-8")
		line= line.replace("\r\n","")
		w , tag = line.split("\t")
		tag = tag.strip()
		if w in dictionary:
			dictionary[w].count_types(tag)
			l = l + dictionary[w].word_types(w)
		else:
			new = word()
			new.count_types(tag)
			dictionary[w] = new

	lexic = open('lexic.txt', 'w')
	lexic.write(l.decode("UTF-8").encode("latin_1"))	
	lexic.close()


def test_function():
	global dictionary
	global t 
	pred = ''
	max_type = ('',0)
	temp_type = ''
	t = '0'
	t = input("Choose a test number 1 or 2: ")
	t = str(t)
	test = open("test_"+t+".txt")
	for word in test:
		word = word.decode("latin_1").encode("UTF-8")
		word = word.replace("\r\n", "")
		if word in dictionary:
			pred = pred+word+"\t"+dictionary[word].most_probable_type()+"\r\n"
			if  max_type[1]<dictionary[word].max_tag():
				max_type = (dictionary[word].most_probable_type(), dictionary[word].max_tag())
		else:
			#if word.isupper():
			#	pred = pred+word+"\t"+"NP"+"\r\n"
			#else:
			#	if word.isdigit():
			#		pred = pred+word+"\t"+'Num'+"\r\n"
			#	else:#if this word is not in the dictionary, we will assigne it the most probable type appearing in the dictionary (in general)
			pred = pred+word+"\t"+max_type[0]+"\r\n"

	file = open("test_"+ t +"_prediction.txt","w")
   	file.write(pred.decode("UTF-8").encode("latin_1"))
   	file.close()

def score_function():
	global t 
	good = 0
	num_lines = 0
	h = ''
	f = ''
	a = ''
	with open("test_"+t+"_prediction.txt") as t1, open("gold_standard_"+t+".txt") as t2:
		for line1, line2 in zip(t1,t2):
			if line1 == line2:
				good += 1
			num_lines += 1


	aa = (good/float(num_lines))*100
	h = h + "Number of hits: " + str(good)
	f = f + "Number of failures: " + str(num_lines - good)
	a = a + "Accuracy: " + str(round(aa,)) + "%"
	#a = a + "Accuracy: " + str(good/float(num_lines))+"->"+str(((good/float(num_lines))*100)round(+"%"
	print h
	print f
	print a


split_corpus()
test_function()
score_function()




			


		












