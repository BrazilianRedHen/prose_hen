import os
import multiprocessing



def run():
	list_of_new_files = [
"2016-feb_JA_10-1097_ACM-0000000000001044_academic-medicine_ten-cate_olle"]

	os.chdir('../pragmatic')
	list_of_files = list()
	for (dirpath, dirname, filename) in os.walk("../pragmatic"):
		list_of_files += [file for file in filename]

	for file in list_of_files:


		if file.replace(".seg", "") in list_of_new_files:

			if file.endswith(".seg"):

				file_name = os.path.splitext(file)[0]
				command = '/home/rafael/semafor/bin/runSemafor.sh ' + str('../pragmatic/'+file + ' /home/rafael/code/prose_hen_17_01_2021_backup/semafor_output/'+file_name + '.sem' + ' 1')
				print(command)
				os.system(command)


p1 = multiprocessing.Process(target=run)

p1.start()
p1.join()
p1.terminate()
