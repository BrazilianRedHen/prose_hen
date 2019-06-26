import os
import uuid
import re
import json
import xml.etree.cElementTree as ET


import dictionaries

# function to indent the XML properly
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i


listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../stanford"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]

lines = []

for file in listOfFiles:
    if file.endswith(".stf"):
        path = file.split('/')

        fileNameNoExt = path[path.__len__()-1].split(".")[0]

        print(fileNameNoExt)

        publicationYear = path[path.__len__()-1].split("_")[0].split("-")[0]

        f=open("../headers/"+publicationYear+"/"+fileNameNoExt+".txt", "r")

        #dealing with the first sets of metadata.
        headerLines = f.readlines()
        for line in headerLines:

            if line.startswith("TTL|"):
                abstractName = line[4:].replace("&#10", "")
                
                

            if line.startswith("SRC|"):
                journalName = line[4:].rstrip().replace("-"," ").upper()
                field = dictionaries.dictionaryFields()[journalName]
                discipline = dictionaries.dictionaryDisciplines()[field]
  

        #inputing metadata text tags on file.
        text = ET.Element('text', abstrct_name=abstractName,  jounal_name=journalName, field=field, discipline=discipline)      
        
        #dealing with the stanfordCoreNLP sstricture and files.
        with open(file) as json_file:
            data = json.load(json_file)
            # tag <p>
            p = ET.SubElement(text, 'p')
            for sentence in data['sentences']:

                for token in sentence['tokens']:
                    lines.append(token['word'] + "\t" + token['pos'] + "\t" + token['lemma'] + "\t" + token['originalText'])
                # tag <s>
                s = ET.SubElement(p, 's').text = "\n"+"\n".join(lines)+"\n"
                lines = []

        
        indent(text)
        
        tree = ET.ElementTree(text)

        tree.write("../vrt/" + fileNameNoExt+".vrt",  encoding="utf8", xml_declaration=True, method="xml")
