import os
import re
import sys 


directory = None

class word():

	def__init__(self, directory):
	self.dir = directory
	self.num_words = ''
	self.vectors = []
	self.frequent_words = ''
	self.N = 10


	def word_counter(self):
	
		for f in os.listdir(self.dir):
			t = open(os.path.join(self.dir, f),'r')
			#this is the regular expression that I want to find an extract from the text  
			exp = re.compile("\w*\w|\w") 
			#return the list of words obtaines from comparing the regular expression
			words = re.findall(exp, t) 
			for word in words:
				if word in self.words:
					self.num_words[word] =+ 1
				else:
					self.num_words[word] = 1
		# esto lo mire del miki pq no se como PUTAS sacar el top, y entonces lo busque en google, y si, es esto del miki 
		# solo que el crea otra funcion para hacerlo, pro sinceramnt no creo que haga falta. 
			self.frequent_words =  sorted(self.num_words.items(), key=lambda k: k[1], reverse=True)[:N]
    


	def vector_creator(self):
		#In here we are going to get the most frequent words and create the feature vectors 

		for f in os.listdir(self.dir):
			total = 0
			counter = dict()

			if f.endswith("_male"):
				gender = "male"
			else: 
				gender = "female"

			t = open(os.path.join(self.dir, f),'r')
			exp = re.compile("\w*\w|\w") 
			words = re.findall(exp, t)
			for word in words:
				if not word == '':
					total += 1
				if word in self.frequent_words:
					counter[word] = self.num_words[word]
					#counter[word] = self.num_words.get(word)
 
			frequency = [float[counter[w]]/float(total) for w in counter.key()]
			self.vectors += [[gender] + freq]

			#esto que he hecho aqui NO SE SI FUNCIONA, LA IDEA ES, ABRO CADA UNO DE LOS TEXTOS DEL DIRECTORY
			#ENTONCES, de cada palabra obtenida tras hacer el regex selection, cuento el num total de palabras
			# para asi tenerlo para calcular la freq mas tarde y entonce digo, si la palabra esra en frequent_words
			# entonces, meteme en counter que es un diccionario su numero de aparaciones.
			#Esto implica que estoy cogiendo el num de apariciones de solo aquellas palabras en la lista de frequent_words de ESE texto
			# LO QUE NO SE ES SI FUNCIONES ESA LINEA DE SELF.NUM_WORDS.GET(WORD) o es la q no esta comentada


	def converter(self): # function to pass vector to arff format 

		arff = open(f, 'w')
		arrf,write('@')

	
		for vector in self.vectors:
            for i in range(1,len(vector)):
                arff.write('{},'.format(vector[i]))
            arff.write(vector[0]+'\n')
        arff.close()





    	