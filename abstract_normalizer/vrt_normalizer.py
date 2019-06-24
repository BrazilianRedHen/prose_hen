import os
import uuid
import re
import json
import xml.etree.cElementTree as ET


import dictionaries


listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../stanford"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]


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
        
  
        with open(file) as json_file:

            data = json.load(json_file)
            for sentence in data['sentences']:
                for word in sentence['tokens']:
                    print (word['word'])


        #inputing metadata text tags on file.
        text = ET.Element('text', abstrct_name=abstractName,  jounal_name=journalName, field=field, discipline=discipline)

    
        #dealing with the stanfordCoreNLP sstricture and files.

        tree = ET.ElementTree(text)
        tree.write("../vrt/" + fileNameNoExt+".vrt",  encoding="utf8", xml_declaration=True, method="xml")
