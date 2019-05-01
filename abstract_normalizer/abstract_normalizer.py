# -*- coding: UTF-8 -*-
import os

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk("../raw"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
lines = 0

nameOfFiles = list()
date = ""
ano = ""
fonte = ""
autor = ""
doi = ""

for file in listOfFiles:
    if file.endswith(".txt"):
        with open(file) as f:
            lines = [line.rstrip('\n') for line in open(file)]
            head, sep, tail = lines[0].partition("FN ")
            
            mes = ""
            ano = ""
            fonte = ""
            autor = ""
            doi = ""

            for l in lines:
                l.replace("\ufeff", "")

                if l.startswith("PD "):
                    date = l.replace("PD ", "")
                    date = date.replace(" ", "-")
                    date = date.lower()

                if l.startswith("PY "):
                    ano = l.replace("PY ", "")

                if l.startswith("DI "):
                    doi = l.replace("DI ", "")

                if l.startswith("SO "):
                    journal = l.replace("SO ", "")
                    fonte += journal.replace(" ", "-").lower()

                if l.startswith("AF "):
                    autorComplete = l.replace("AF ", "")
                    autorLast, sep, autorFirstComplete = autorComplete.partition(', ')
                    autorLast = autorLast.replace(" ", "-").lower()
                    

                    aux = 2 # this is two taking into consideration that an abreviated name is the first letter of the name plus a comma eg. D.
                    autorFirstList = autorFirstComplete.split(" ")
                    if len(autorFirstList) == 1 and len(autorFirstList[0]) != aux:
                        autorFirst = autorFirstList[0]
                    else:
                        
                        for autorName in autorFirstList:
                            if len(autorName) > aux and len(autorName) != aux:
                                autorFirst = autorName
                                break
                            else:
                                autorFirst = ""
                    autorFirst = autorFirst.lower()

            #start assembling string
            stringFileName = str(ano)

            if date != "":
                stringFileName += "-"
                stringFileName += str(date)
            else:
                stringFileName += "00"

            #separating Date and DOI putting the annotation name
            stringFileName += "_JA_"
            
            if doi != "":
                stringFileName += doi
            else:
                stringFileName += "00-0000_0000000000000000"

            #separating DOI and file source
            stringFileName += "_"+str(fonte)

            #adding first author name
            stringFileName += "_"
            stringFileName += str(autorLast)
            if autorFirst != "":
                stringFileName += "_"
                stringFileName += str(autorFirst)

            #slashes are underscores
            #dots are dashes
            stringFileName = stringFileName.replace("/", "_")
            stringFileName = stringFileName.replace(".", "-")

            #adding extention
            stringFileName += ".txt"


            nameOfFiles.append(stringFileName)

            with open("../abstracts/"+ano+"/"+stringFileName, "w+") as fileReady:
                for lineInFile in f:
                    fileReady.write(lineInFile)

print(nameOfFiles)
