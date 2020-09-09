import os
import multiprocessing

def run():
	command = 'dois cores'
	os.system(command)
	os.chdir('../pragmatic')
	list_of_files = list()
	for (dirpath, dirname, filename) in os.walk("../pragmatic"):
		list_of_files += [file for file in filename]

	for file in list_of_files:
		if file.endswith(".seg"):
			file_name = os.path.splitext(file)[0]
			command = './home/zilli/semafor/bin/runSemafor.sh' + str('../pragmatic/'+file + ' ../semafor_output/'+file_name + '.sem' + ' 1')
			os.system(command)
	os.system('exit')

p1 = multiprocessing.Process(target=run)

p1.start()
p1.join()
p1.terminate()

#Obs: The directories needs to be changed, according where was installed the semafor and prose_hen folders
