import os
import uuid
import re

import dictionaries


listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../stanford"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]


for file in listOfFiles:
    if file.endswith(".stf"):
        path = file.split('/')

        fileNameNoExt = path[path.__len__()-1].split(".")[0]

        publicationYear = path[path.__len__()-1].split("_")[0].split("-")[0]

        f=open("../headers/"+publicationYear+"/"+fileNameNoExt+".txt", "r")



        headerLines = f.readlines()
        for line in headerLines:

            if line.startswith("TTL|"):
                abstractName = line[4:]
                
                print("Abstract Name: "+ abstractName)

            if line.startswith("SRC|"):
                journalName = line[4:].rstrip().replace("-"," ").upper()
                field = dictionaries.dictionaryFields()[journalName]
                discipline = dictionaries.dictionaryDisciplines()[field]
                
                print("Journal Name: "+ journalName+ "\nField Name: "+ field + "\nDiscipline Name: "+  discipline+"\n\n")



        # completeDate = path[path.__len__()-1].split("_")[0]

        # completePath = path[path.__len__()-2]+"/   "+path[path.__len__()-1]
        # completePath = completePath.replace("..", ".")
        # completePath = completePath.replace(" ", "")

        # print(completePath)

        # line1 = "TOP|"+completeDate+"|"+completePath+'\n'

        # line2 = "COL|Journal Abstracts, Red Hen Lab"+'\n'

        # line3 = "UID|"+uuid.uuid4().hex+'\n'

        # line5 = "CMT|"+'\n'

        # line6 = "CC1|ENG"+'\n'

        # line9 = "END|"+completeDate+"|"+completePath+'\n'


        # with open(file) as f:
        #     lines = [line.rstrip('\n') for line in open(file)]

        #     #SEARCH FOR TITLE
        #     r = re.search("TI ((.*?\n)+)SO", "\n".join(map(str, lines)))

        #     if r:
        #         line7 = "TTL|"+r.group(1).strip().replace("\n", " ").replace("    ", " ")+"\n"

        #     #SEARCH FOR ABSTRACT CONTENTS
        #     r = re.search("AB ([\w\W]*?)(?=\n[A-Z]{2}\s)", "\n".join(map(str, lines)))            

        #     if r: 
        #         line8 = "CON|"+ r.group(1).strip().replace("\n", " ").replace("    ", " ")+"\n"

        #     #FOREACH LINE TO GATHER NAME OF
        #     for l in lines:
        #         l.replace("\ufeff", "")

        #         if l.startswith("SO "):
        #             subLine = l[2:]
        #             trimmedSubLine = subLine.strip()
        #             line4 = "SRC|"+trimmedSubLine+'\n'

        #     stringFinal = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9
        #     with open("../headers/" + completePath, "w+") as fileReady:
        #         fileReady.write(stringFinal)

