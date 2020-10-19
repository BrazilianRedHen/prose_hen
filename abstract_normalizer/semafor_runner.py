import os
import multiprocessing
import numpy as np

import data_gatherer

def run():
	
	# os.chdir('../pragmatic')
	# list_of_files = list()
	# for (dirpath, dirname, filename) in os.walk("../pragmatic"):
	# 	list_of_files += [file for file in filename]
	list_of_files = data_gatherer.get_files_need_parsing("semafor_output", "sem") 

	broken_list = np.array_split(list_of_files, 5)
	#broken_list = list()
	#broken_list.append(list_of_files)

	slurm_count = 0
	for small_list_of_files in broken_list:
		shell_file = """#!/bin/bash
#SBATCH -c 4
#SBATCH --mem=40g

"""
		for file in small_list_of_files:
			shell_file += '/mnt/rds/redhen/gallina/home/ngc17/semafor/bin/runSemafor.sh' + str('/mnt/rds/redhen/gallina/home/ngc17/prose_hen/pragmatic/' + file + '.seg /mnt/rds/redhen/gallina/home/ngc17/prose_hen/semafor_output/' + file + '.sem' + ' 1 \n')
	
		print(shell_file)
		with open("../semafor"+str(slurm_count)+".slurm", "w+") as file_ready:
			file_ready.write(shell_file)
		slurm_count = slurm_count + 1


p1 = multiprocessing.Process(target=run)

p1.start()
p1.join()
p1.terminate()

