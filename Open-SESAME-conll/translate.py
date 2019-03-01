import json

with open('sample_18x_predicted-args.conll') as f:
    content = f.readlines()

line_of_sentence_index = 1
first_sentence_line_index = 0
last_sentence_line_index = 0
sentences_with_tabs = list()
for line in content:

    if line.split('\t')[0] == str(line_of_sentence_index):
        line_of_sentence_index += 1
    else:
        sentences_with_tabs.append(content[first_sentence_line_index:last_sentence_line_index:])
        first_sentence_line_index = last_sentence_line_index
        line_of_sentence_index = 1
    last_sentence_line_index += 1
    if line == '\n':
        first_sentence_line_index += 1

sentences = list()

sentence_with_no_spaces_old = ''
sentence_with_no_spaces = ''

sentence_group = list()

for sentence_with_tabs in sentences_with_tabs:
    target = ''
    frame = ''
    args = list()
    word_index = 1
    counter = 1
    sentence_with_no_spaces_old = sentence_with_no_spaces
    sentence_with_no_spaces = ''
    for line_with_tabs in sentence_with_tabs:
        line_with_tabs = line_with_tabs.replace('\n', '')
        columns = line_with_tabs.split('\t')
        sentence_with_no_spaces += columns[1]
        target = columns[12] if columns[12] != '_' else target
        word_index = columns[0] if columns[12] != '_' else word_index
        frame = columns[13] if columns[13] != '_' else frame
        args.append({
            'ID': columns[0],
            'FORM': columns[1],
            'PPOS': columns[5],
            'APREDn': columns[14]
        })
        counter += 1
    # print(sentence_with_no_spaces, ' ', sentence_with_no_spaces_old)
    if sentence_with_no_spaces_old == sentence_with_no_spaces:
        sentence_group.append({
            'ID': word_index,
            'FILLPRED': target,
            'PRED': frame,
            'APRED': args
        })
    else:
        if sentence_group.__len__() > 0:
            sentences.append(sentence_group)
        sentence_group = list()

print(json.dumps(sentences))

