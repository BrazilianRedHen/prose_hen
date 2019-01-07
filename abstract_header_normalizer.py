import os;
import sys;

listOfFiles = list()
for (dirpath, dirnamonth, filenamonth) in os.walk("abstracts"):
	listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]
lines = 0

nameOfFiles = list()
month = ""
year = ""
completeDate = ""
maskedDate = ""
filename_ = ""
journalInitials = ""
fileContent = ""

for file in listOfFiles:

    if file.endswith(".txt"):

        with open(file) as f:
            lines = [line.rstrip('\n') for line in open(file)]

    	
    		print(*lines, sep = x+" \n")  
		sys.exit()

            # head, sep, tail = lines[0].partition("FN ")
            # fonte = tail.replace(" ", "_").lower()


            # for l in lines:
            # 	print(l)
            #     l.replace("\ufeff", "")

            #     if l.startswith("PD "):
            #         month = l.replace("PD ", "")
            #         month = month.replace(" ", "-")
            #         month = month.replace("JAN", "01")
            #         month = month.replace("FEB", "02")
            #         month = month.replace("MAR", "03")
            #         month = month.replace("APR", "04")
            #         month = month.replace("MAY", "05")
            #         month = month.replace("JUN", "06")
            #         month = month.replace("JUL", "07")
            #         month = month.replace("AUG", "08")
            #         month = month.replace("SEP", "09")
            #         month = month.replace("OCT", "10")
            #         month = month.replace("NOV", "11")
            #         month = month.replace("DEC", "12")

            #     if l.startswith("PY "):
            #         year = l.replace("PY ", "")

            #     if l.startswith("DI "):
            #         doi = l.replace("DI ", "")

            #     if l.startswith("SO "):
            #         journal = l.replace("SO ", "")
            #         fonte += "-"
            #         fonte += journal.replace(" ", "_").lower()

            #     if l.startswith("AU "):
            #         autorL = l.replace("AU ", "")
            #         autor, sep, tail = autorL.partition(', ')


			
