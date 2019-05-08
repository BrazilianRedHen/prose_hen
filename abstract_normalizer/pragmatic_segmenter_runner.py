import os
listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../headers"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]

for file in listOfFiles:
    if file.endswith(".txt"):
        path = file.split('/')
        path = path[path.__len__()-1]
        path = path.replace("..", ".")

        print(path)

        sendToPragmatic = ''

        with open(file) as f:
            lines = [line.rstrip('\n') for line in open(file)]
            head, sep, tail = lines[0].partition("FN ")

            for l in lines:
                l.replace("\ufeff", "")


                if l.startswith("SRC|"):
                    sendToPragmatic = l[4:].capitalize().strip() + '.' + '\n'

                if l.startswith("TTL|"):
                    sendToPragmatic += l[4:].strip() + '.' + '\n'

                if l.startswith("CON|"):
                    sendToPragmatic += " "
                    sendToPragmatic += l[4:]

            with open("../pragmatic/cache/" + path[:-3]+'seg', "w+") as fileReady:
                fileReady.write(sendToPragmatic)

            pragmaticReturn = os.system('ruby ps.rb "' + path[:-3]+'seg' + '"')
print("end")