# -*- coding: UTF-8 -*-
import os
import uuid
import re
import json
import pandas as pd


import dictionaries

def gather_all_files():
    listOfFiles = list()
    for (dirpath, dirnamonth, filenamonth) in os.walk("../headers"):
        listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]
    return listOfFiles

def gather_file_data():
    file_list = list()
    for file in gather_all_files():
        if file.endswith(".txt"):
            this_file = {}
            path = file.split('/')
            path = path[path.__len__()-1]
            path = path.replace("..", ".")
            path = path.replace(".txt", "")
            this_file["name"] = path


            raw_content = open(file, "r")

            lines = raw_content.readlines()
            for line in lines:
                if line.startswith("SRC|"):
                    this_file["journalName"] = line[4:].rstrip().replace("-"," ").upper().replace("\n","")
                    this_file["field"] = dictionaries.dictionaryFields()[this_file["journalName"]].replace("\n","")
                    this_file["discipline"] = dictionaries.dictionaryDisciplines()[this_file["field"]].replace("\n","")
                    file_list.append(this_file)
    return file_list

def gather_file_data_by_discipline(discipline):    
    return [file for file in gather_file_data() if file["discipline"] == discipline]
        

print(gather_file_data_by_discipline("HARD SCIENCES"))