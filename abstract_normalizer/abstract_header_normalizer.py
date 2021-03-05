import os
import uuid
import re

listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("../abstracts"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]

files_to_run = ["2015-feb_JA_10-1097_ACM-0000000000000549_academic-medicine_brydges_ryan",
"2015-aug_JA_10-1097_ACM-0000000000000786_academic-medicine_cook_david",
"2015-jul_JA_10-1097_ACM-0000000000000655_academic-medicine_dyrbye_liselotte",
"2015-apr_JA_10-1097_ACM-0000000000000641_academic-medicine_ripp_jonathan",
"2015-jun_JA_10-1097_ACM-0000000000000700_academic-medicine_cruess_richard",
"2015-nov_JA_10-1097_ACM-0000000000000894_academic-medicine_martimianakis_maria",
"015-jun_JA_10-1097_ACM-0000000000000725_academic-medicine_wald_hedy",
"2015-nov_JA_10-1097_ACM-0000000000000939_academic-medicine_ericsson_anders",
"2015-apr_JA_10-1097_ACM-0000000000000586_academic-medicine_chen_carrie",
"2015-may_JA_10-1097_ACM-0000000000000560_academic-medicine_telio_summer",
"2015-may_JA_10-1097_ACM-0000000000000661_academic-medicine_burke_sara",
"2015-feb_JA_10-1097_ACM-0000000000000552_academic-medicine_carnes_molly",
"2015-sep_JA_10-1097_ACM-0000000000000842_academic-medicine_jennings",
"2016-feb_JA_10-1097_ACM-0000000000001044_academic-medicine_ten-cate_olle.",
"2016-aug_JA_10-1097_ACM-0000000000001250_academic-medicine_freund_karen.",
"2016-oct_JA_10-1097_ACM-0000000000001204_academic-medicine_englander_robert",
"2016-feb_JA_10-1097_ACM-0000000000001045_academic-medicine_rekman_janelle",
"2016-sep_JA_10-1097_ACM-0000000000001138_academic-medicine_jackson_eric",
"2016-jun_JA_10-1097_ACM-0000000000001114_academic-medicine_cook_david",
"2016-feb_JA_10-1097_ACM-0000000000000913_academic-medicine_cruess_richard"]


for file in listOfFiles:
    if file.endswith(".txt"):
        path = file.split('/')


        completeDate = path[path.__len__()-1].split("_")[0]

        completePath = path[path.__len__()-2]+"/   "+path[path.__len__()-1]
        completePath = completePath.replace("..", ".")
        completePath = completePath.replace(" ", "")

        print(completePath.replace(".txt", ""))

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
