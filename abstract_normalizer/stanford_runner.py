from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/var/python/stanford-corenlp-full-2018-10-05')


text = 'Guangdong University of Foreign Studies is located in Guangzhou. ' \
       'GDUFS is active in a full range of international cooperation and exchanges in education. '

props={'annotators': 'tokenize,ssplit,pos','pipelineLanguage':'en','outputFormat':'json'}
print nlp.annotate(text, properties=props)
nlp.close()