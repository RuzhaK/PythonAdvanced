import os
import pathlib

directory=input()
directory_dict={} #{'.py':['program1.py', ['program2.py'], '.html':['index.html']]}
for root, directory, files in os.walk(directory):
    for file in files:
        extension=file.split('.')[-1]
        if extension not in directory_dict:
            directory_dict[extension]=[]
        directory_dict[extension].append(file)
final_output=''
for extension in sorted(directory_dict.keys()):
    final_output+='.'+extension+'\n'
    for file in sorted(directory_dict[extension]):
        final_output+=f'---{file}\n'

desktop_path=str(pathlib.Path.home())+os.path.sep+'Desktop'
report_txt_path =desktop_path+os.path.sep+'report.txt'
# os.path.sep e universal separator

with open(report_txt_path,'x') as file:
    file.write(final_output)

