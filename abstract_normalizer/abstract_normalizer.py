import os;

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk("."):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
lines = 0

nameOfFiles = list()
mes = ""
ano = ""
fonte = ""
autor = ""
doi = ""

for file in listOfFiles:
    if file.endswith(".txt"):
        with open(file) as f:
            lines = [line.rstrip('\n') for line in open(file)]
            head, sep, tail = lines[0].partition("FN ")
            fonte = tail.replace(" ", "_").lower()

            for l in lines:
                l.replace("\ufeff", "")

                if l.startswith("PD "):
                    mes = l.replace("PD ", "")
                    mes = mes.replace(" ", "-")
                    mes = mes.replace("JAN", "01")
                    mes = mes.replace("FEB", "02")
                    mes = mes.replace("MAR", "03")
                    mes = mes.replace("APR", "04")
                    mes = mes.replace("MAY", "05")
                    mes = mes.replace("JUN", "06")
                    mes = mes.replace("JUL", "07")
                    mes = mes.replace("AUG", "08")
                    mes = mes.replace("SEP", "09")
                    mes = mes.replace("OCT", "10")
                    mes = mes.replace("NOV", "11")
                    mes = mes.replace("DEC", "12")

                if l.startswith("PY "):
                    ano = l.replace("PY ", "")

                if l.startswith("DI "):
                    doi = l.replace("DI ", "")

                if l.startswith("SO "):
                    journal = l.replace("SO ", "")
                    fonte += "-"
                    fonte += journal.replace(" ", "_").lower()

                if l.startswith("AU "):
                    autorL = l.replace("AU ", "")
                    autor, sep, tail = autorL.partition(', ')

            stringFileName = str(ano)

            if mes != "":
                stringFileName += "-"
                stringFileName += str(mes)
            else:
                stringFileName += "00"

            stringFileName += "_"
            stringFileName += str(fonte)

            if doi != "":
                stringFileName += "-"
                stringFileName += doi
            else:
                stringFileName += "00.0000∕0000000000000000"

            stringFileName += "-"
            stringFileName += str(autor)
            stringFileName += ".txt"

            stringFileName = stringFileName.replace("/", "\u2215")

            mes = ""
            ano = ""
            fonte = ""
            autor = ""
            doi = ""

            nameOfFiles.append(stringFileName)

            with open("testes/"+stringFileName, "w+") as fileReady:
                for lineInFile in f:
                    fileReady.write(lineInFile)

print(nameOfFiles)
