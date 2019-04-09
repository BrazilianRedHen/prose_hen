import os
import uuid

listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../abstracts"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]


for file in listOfFiles:
    if file.endswith(".txt"):
        caminho = file.split('/')
        caminho = caminho[caminho.__len__()-2]+"/"+caminho[caminho.__len__()-1]
        caminho = caminho.replace("..", ".")
        caminho = caminho.replace("\xe2\x88\x95", "**")

        print(caminho)

        stringData = caminho[:10]
        completeDate = stringData.split('-')
        completeDate = ''.join(completeDate) + '12.0000'

        line1 = "TOP|"+completeDate+"|"+caminho+'\n'

        line2 = "COL|Journal Abstracts, Red Hen Lab"+'\n'

        line3 = "UID|"+uuid.uuid4().hex+'\n'

        line5 = "CMT|"+'\n'

        line6 = "CC1|ENG"+'\n'

        line9 = "END|"+completeDate+"|"+caminho+'\n'

        line7_1 = ""

        line7_2 = ""


        with open(file) as f:
            lines = [line.rstrip('\n') for line in open(file)]
            head, sep, tail = lines[0].partition("FN ")
            fonte = tail.replace(" ", "_").lower()

            for l in lines:
                l.replace("\ufeff", "")

                if l.startswith("TI "):
                    subLine = l[2:]
                    trimmedSubLine = subLine.strip()
                    line7_1 = "TTL|"+trimmedSubLine

                if l.startswith("   "):
                    subLine = l[2:]
                    trimmedSubLine = subLine.strip()
                    line7_2 = trimmedSubLine

                if l.startswith("SO "):
                    subLine = l[2:]
                    trimmedSubLine = subLine.strip()
                    line4 = "SRC|"+trimmedSubLine+'\n'

                if l.startswith("AB "):
                    subLine = l[2:]
                    trimmedSubLine = subLine.strip()
                    line8 = "CON|"+trimmedSubLine+'\n'

            stringFinal = line1 + line2 + line3 + line4 + line5 + line6 + line7_1 + " " +line7_2 + '\n' + line8 + line9
            with open("../headers/" + caminho, "w+") as fileReady:
                fileReady.write(stringFinal)
