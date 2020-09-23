import os
import multiprocessing

def run():
	shell_file = """#!/bin/bash
#SBATCH -c 4
#SBATCH --mem=40g

"""
	os.chdir('../pragmatic')
	list_of_files = list()
	for (dirpath, dirname, filename) in os.walk("../pragmatic"):
		list_of_files += [file for file in filename]

	for file in list_of_files:
		if file.endswith(".seg"):
			file_name = os.path.splitext(file)[0]
			shell_file += '/mnt/rds/redhen/gallina/home/ngc17/semafor/bin/.runSemafor.sh' + str('/mnt/rds/redhen/gallina/home/ngc17/prose_hen/pragmatic/'+file + ' /mnt/rds/redhen/gallina/home/ngc17/prose_hen/semafor_output/'+file_name + '.sem' + ' 1 &\n')
	
	print(shell_file)
	with open("../semafor.slurm", "w+") as file_ready:
		file_ready.write(shell_file)


p1 = multiprocessing.Process(target=run)

p1.start()
p1.join()
p1.terminate()

