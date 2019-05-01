import os
import uuid
import re

listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../abstracts"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]


for file in listOfFiles:
    if file.endswith(".txt"):
        path = file.split('/')

        completeDate = path[path.__len__()-1].split("_")[0]

        completePath = path[path.__len__()-2]+"/   "+path[path.__len__()-1]
        completePath = completePath.replace("..", ".")
        completePath = completePath.replace(" ", "")

        print(completePath)

        line1 = "TOP|"+completeDate+"|"+completePath+'\n'

        line2 = "COL|Journal Abstracts, Red Hen Lab"+'\n'

        line3 = "UID|"+uuid.uuid4().hex+'\n'

        line5 = "CMT|"+'\n'

        line6 = "CC1|ENG"+'\n'

        line9 = "END|"+completeDate+"|"+completePath+'\n'


        with open(file) as f:
            lines = [line.rstrip('\n') for line in open(file)]

            #SEARCH FOR TITLE
            r = re.search("TI ((.*?\n)+)SO", "\n".join(map(str, lines)))

            if r:
                line7 = "TTL|"+r.group(1).strip().replace("\n", " ").replace("    ", " ")+"\n"

            #SEARCH FOR ABSTRACT CONTENTS
            r = re.search("AB ([\w\W]*?)(?=\n[A-Z]{2}\s)", "\n".join(map(str, lines)))            

            if r: 
                line8 = "CON|"+ r.group(1).strip().replace("\n", " ").replace("    ", " ")+"\n"

            #FOREACH LINE TO GATHER NAME OF
            for l in lines:
                l.replace("\ufeff", "")

                if l.startswith("SO "):
                    subLine = l[2:]
                    trimmedSubLine = subLine.strip()
                    line4 = "SRC|"+trimmedSubLine+'\n'

            stringFinal = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9
            with open("../headers/" + completePath, "w+") as fileReady:
                fileReady.write(stringFinal)
