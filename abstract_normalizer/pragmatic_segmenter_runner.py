import os
listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../headers"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]

for file in listOfFiles:
    if file.endswith(".txt"):
        caminho = file.split('/')
        caminho = caminho[caminho.__len__()-1]
        caminho = caminho.replace("..", ".")

        print(caminho)

        sendToPragmatic = ''

        with open(file) as f:
            lines = [line.rstrip('\n') for line in open(file)]
            head, sep, tail = lines[0].partition("FN ")
            fonte = tail.replace(" ", "_").lower()

            for l in lines:
                l.replace("\ufeff", "")


                if l.startswith("SRC|"):
                    sendToPragmatic = l[4:].capitalize().strip() + '.' + '\n'

                if l.startswith("TTL|"):
                    sendToPragmatic += l[4:].strip() + '.' + '\n'

                if l.startswith("CON|"):
                    sendToPragmatic += " "
                    sendToPragmatic += l[4:]

            with open("../pragmatic/cache/" + caminho[:-3]+'seg', "w+") as fileReady:
                fileReady.write(sendToPragmatic)

            pragmaticReturn = os.system('ruby ps.rb "' + caminho[:-3]+'seg' + '"')
print("end")