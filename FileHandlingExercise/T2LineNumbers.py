import string
lines=[]
with open('test.txt','r') as file:
    lines=file.readlines()
i=0
with open('output.txt','x') as file:
    for i, line in enumerate(lines):
        line_number = f'Line{i + 1}:'
        letter_count = len(list(filter(lambda x: x in string.ascii_letters, line)))
        punc_count = len(list(filter(lambda x: x in string.punctuation, line)))

        file.write(f'{line_number}{line[:-1]}({letter_count})({punc_count})\n')