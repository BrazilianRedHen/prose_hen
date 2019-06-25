# -*- coding: UTF-8 -*-
import os
import json
import hashlib

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk("../stanford/"):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
lines = 0

nameOfFiles = list()
vrt = "<?xml version='1.0' encoding='UTF-8'?>"
for file in listOfFiles:
    if file.endswith(".stf"):
        with open(file) as f:
            identification = file.split('/')
            stanford = json.loads(f.read())
            string_id_hash = hashlib.md5(identification[-1].split('.')[0:-1][0].encode())
            vrt += "\n<text id='" + string_id_hash.hexdigest() + "' >"
            vrt += "\n<p>"
            for s in stanford["sentences"]:
                vrt += "\n<s>\n"
                for token in s["tokens"]:
                    vrt += token["word"]
                    vrt += "\t"
                    vrt += token["pos"]
                    vrt += "\t"
                    vrt += token["lemma"]
                    vrt += "\t"
                    vrt += token["word"]
                    vrt += '\n'
                vrt += "</s>"
            vrt += "\n</p>\n</text>"            

with open('corpus.vrt', "w") as vrt_file:
    vrt_file.write(vrt)
