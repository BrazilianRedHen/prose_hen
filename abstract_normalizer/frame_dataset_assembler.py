# -*- coding: UTF-8 -*-
import os
import uuid
import re
import json
import pandas as pd


import dictionaries
import data_gatherer


def gather_list_of_files():
    listOfFiles = list()
    listOfFileInformation = data_gatherer.gather_file_data()
    for fileInformation in listOfFileInformation:
        listOfFiles.append("../semafor_output/" + fileInformation["name"] + ".sem")

    return listOfFiles


def solving_complete_path(file_name):
    complete_path = file_name.replace("..", ".")
    complete_path = complete_path.replace(" ", "")
    complete_path = complete_path.replace(".sem", "")

    return complete_path


def solving_metadata(header_lines):
    this_file = {}
    for line in header_lines:
        
        if line.startswith("TTL|"):
            this_file["abstractName"] = line[4:].replace("&#10", "").replace("\ufeff", "").replace("\n","")
            
        if line.startswith("SRC|"):
            this_file["journalName"] = line[4:].rstrip().replace("-"," ").upper().replace("\n","")
            this_file["field"] = dictionaries.dictionaryFields()[this_file["journalName"]].replace("\n","")
            this_file["discipline"] = dictionaries.dictionaryDisciplines()[this_file["field"]].replace("\n","")

    return this_file


semafor_list = list()
metadata_list = list()
count = 0
for file in gather_list_of_files():

    if file.endswith(".sem"):
    #if file == "../semafor_output/2015-jun_JA_10-1097_ACM-0000000000000700_academic-medicine_cruess_richard2.sem":
        path = file.split('/')
        file = file.replace("'", "")


        completePath = solving_complete_path(path[len(path)-1])

        publicationYear = path[path.__len__()-1].split("_")[0].split("-")[0]


        with open(file) as f:
            lines = [line.rstrip('\n') for line in f]
            
            semafor_list.append("{\"" + completePath + "\": [" + ", ".join(lines) + "]}")

        f = open("../headers/" + publicationYear + "/" + completePath + ".txt", "r")

        print(f.readlines) 

        metadata_list.append(solving_metadata(f))

        print(metadata_list)

        count = count + 1

allFilesSemafor = json.loads("{\"all_files_semafor\": ["+", ".join(semafor_list)+"]}")


print("ammount of files in semafor_output: "+str(count))

filename_list = list()
abstract_name_list = list() 
journal_list = list() 
field_list = list() 
discipline_list = list() 
sentence_count_list = list() 
frame_list = list() 
lexical_unit_list = list() 
lexical_unit_start_list = list() 
lexical_unit_end_list = list() 
frame_elements_list = list() 
complete_phrase_list = list() 

string_csv = "filename,abstract_name,abstract_name,journal,field,discipline,sentence_count,frame,lexical_unit,lexical_unit_start,lexical_unit_end,frame_elements,compleate phrase\r\n"
count_abstracts = 1
for index, abstract in enumerate(allFilesSemafor["all_files_semafor"]):
    abstractNameKey = abstract.keys()[0]

    abstract_string_csv = abstractNameKey + "," + metadata_list[index]["abstractName"] + "," + metadata_list[index]["journalName"] + "," + metadata_list[index]["field"] + "," + metadata_list[index]["discipline"]

    
    #NECESSÁRIO MERGULHO NO ARQUIVO DO SEMAFOR

    sentence_count = 0
    for sentence in abstract[abstractNameKey]:
        complete_phrase = " ".join( sentence["tokens"])
        #print(str(sentence_count) +": "+ " ".join( sentence["tokens"]))


        #verify if there is a frame in the sentence, if not, just jump it...
        if sentence["frames"] != []:

            for item in sentence["frames"]:
                frame_type = item["target"]["name"]
                lexical_unit = item["target"]["spans"][0]["text"]
                start_word_index_in_sentece = str(item["target"]["spans"][0]["start"])
                end_word_index_in_sentece = str(item["target"]["spans"][0]["end"])
                

                sentence_frame_elements_list = list()
                for annotationSet in item["annotationSets"]:
                    for frameElement in annotationSet["frameElements"]:
                        sentence_frame_elements_list.append("{ \"frameElement\": \""+ frameElement["name"] + "\", \"starts\": " + str(frameElement["spans"][0]["start"]) + ", \"ends\": " + str(frameElement["spans"][0]["end"]) + ", \"word\": \"" + frameElement["spans"][0]["text"] + "\" }")

                line = abstract_string_csv + "," + str(sentence_count) + "," + frame_type + "," + lexical_unit + "," + start_word_index_in_sentece + "," + end_word_index_in_sentece + ",\"[" + ", ".join(sentence_frame_elements_list) + "]\",     " + complete_phrase + "\r\n"

                string_csv = string_csv + line

                filename_list.append(abstractNameKey)
                abstract_name_list.append(metadata_list[index]["abstractName"]) 
                journal_list.append(metadata_list[index]["journalName"]) 
                field_list.append(metadata_list[index]["field"]) 
                discipline_list.append(metadata_list[index]["discipline"]) 
                sentence_count_list.append(sentence_count) 
                frame_list.append(frame_type) 
                lexical_unit_list.append(lexical_unit) 
                lexical_unit_start_list.append(start_word_index_in_sentece) 
                lexical_unit_end_list.append(end_word_index_in_sentece) 
                frame_elements_list.append(", ".join(sentence_frame_elements_list)) 
                complete_phrase_list.append(complete_phrase) 


        sentence_count = sentence_count + 1

                
        
    #if count_abstracts == 2 :
        #break

    count_abstracts = count_abstracts + 1

print("Number of processed files: "+ str(count_abstracts))

my_dict = {  "filename": filename_list,
            "abstract_name": abstract_name_list,
            "journal": journal_list,
            "field": field_list,
            "discipline": discipline_list,
            "sentence_count": sentence_count_list,
            "frame": frame_list,
            "lexical_unit": lexical_unit_list,
            "lexical_unit_start": lexical_unit_start_list,
            "lexical_unit_end": lexical_unit_end_list,
            "frame_elements": frame_elements_list,
            "complete_phrase": complete_phrase_list}

for phrase in my_dict["complete_phrase"]:

    print(phrase)

df = pd.DataFrame(my_dict)

df.to_csv('../datasets/datamodel_tmp.csv', index=False) 