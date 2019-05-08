import os
import uuid
import re
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/var/python/stanford-corenlp-full-2018-10-05')

props={'annotators': 'tokenize,ssplit,pos,lemma','pipelineLanguage':'en','outputFormat':'json'}

listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../pragmatic"):
	listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]


for file in listOfFiles:
	caminho = file.split('/')
	if caminho[2] != "cache":
		stanfordFileName = caminho[2]
		stanfordFileName = os.path.splitext(stanfordFileName)[0]
		
		with open(file) as f:

			text = f.read()

			annotatedText = nlp.annotate(text, properties=props)

			with open("../stanford/" + stanfordFileName+".stf", "w+") as fileReady:
				fileReady.write(annotatedText)

nlp.close()
print "end"

# text = 'Guangdong University of Foreign Studies is located in Guangzhou. ' \
#        'GDUFS is active in a full range of international cooperation and exchanges in education. '



