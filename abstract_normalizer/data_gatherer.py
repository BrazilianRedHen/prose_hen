# -*- coding: UTF-8 -*-
import os
import uuid
import re
import json
import pandas as pd


import dictionaries

def gather_all_files(folder_name):
    listOfFiles = list()
    for (dirpath, dirnamonth, filenamonth) in os.walk("../"+folder_name):
        listOfFiles += [os.path.join(dirpath, file) for file in filenamonth]
    return listOfFiles

def gather_file_data():
    file_list = list()
    for file in gather_all_files("headers"):
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

def get_file_names_list(folder_name, file_extension):
    file_names = list()
    for file in gather_all_files(folder_name):
        if file.endswith("."+file_extension):
            this_file = {}
            path = file.split('/')
            path = path[path.__len__()-1]
            path = path.replace("..", ".")
            path = path.replace("."+file_extension, "")
            file_names.append(path)
    return file_names

def get_files_need_parsing(parser_folder, extension_parsed):
    pragmatic_files = get_file_names_list("pragmatic", "seg")
    frame_parsed_files = get_file_names_list(parser_folder, extension_parsed)
    
    need_parsing = list()

    for file in pragmatic_files:
        if file not in frame_parsed_files:
            need_parsing.append(file)

    return need_parsing
    


#TESTS        

get_files_need_parsing("semafor_output/new_run", "sem")

#print(gather_file_data_by_discipline("HARD SCIENCES"))