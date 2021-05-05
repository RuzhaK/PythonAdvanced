import os
try:
    os.remove('new_file.txt')
    print('Successfully deleted')
except FileNotFoundError:
    print('File already deleted!')

    # alternative
file_path='new_file.txt'
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')