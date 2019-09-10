import os
import uuid
import re
import json
import hashlib

list_of_files = list()
for (dirpath, dirname, filename) in os.walk("../semafor_output"):
    list_of_files += [os.path.join(dirpath, file) for file in filename]

for file in list_of_files:
    if file.endswith(".json"):
        path = file.split('/')
        fileNameNoExt = path[path.__len__() - 1].split(".")[0]
        f = open(file, "r")

        sem_file = f.readlines()

        # Lista de frames e elements (arquivo inteiro)
        complete_list_frames = list()
        complete_list_elements = list()

        for line in sem_file:

            # lista de frames (linha)
            list_frames = list()
            list_elements = list()

            json_line = json.loads(line)
            json_frames = json_line.get('frames')
            json_tokens = json_line.get('tokens')

            for frame in json_frames:
                target = frame.get('target')
                elements = frame.get('annotationSets')[0].get('frameElements')

                for spans in target.get('spans'):
                    if ' ' in spans.get('text'):
                        spaces_between = range(spans.get('start'), spans.get('end'))
                        i = 0
                        for lexical_un in spans.get('text').split(" "):
                            list_frames.append({
                                "wordIndex": spaces_between[i],
                                "name": target.get('name'),
                                "text": lexical_un
                            })
                            i += 1
                    else:
                        list_frames.append({
                            "wordIndex": spans.get('start'),
                            "name": target.get('name'),
                            "text": spans.get('text')
                        })

                for element in elements:
                    if ' ' in element.get('spans')[0].get('text'):
                        spaces_between = range(element.get('spans')[0].get('start'), element.get('spans')[0].get('end'))
                        i = 0
                        for lexical_un in element.get('spans')[0].get('text').split(" "):
                            list_elements.append({
                                "wordIndex": spaces_between[i],
                                "name": element.get('name'),
                                "text": lexical_un
                            })
                            i += 1
                    else:
                        list_elements.append({
                            "wordIndex": element.get('spans')[0].get('start'),
                            "name": element.get('name')
                        })

            complete_list_frames.append(list_frames)
            complete_list_elements.append(list_elements)

        file_json_output = {
            "frames": complete_list_frames,
            "elements": complete_list_elements
        }

        with open('../../parser_out/data.json', 'w') as outfile:
            json.dump(file_json_output, outfile)
