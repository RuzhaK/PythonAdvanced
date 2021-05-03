import os

line=input()


def create_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    with open(filename,'x'):
        pass

def append_line_to_file(filename, line):
    if not os.path.isfile(filename):
        with open(filename,'x'):
            pass

    with open(filename, 'a') as file:
        file.write(f'{line}\n')



def replace_string_in_file(filename, oldstring, newstring):
    if not os.path.exists(filename):
        print("An error occured")
        return
    with open(filename,'r') as file:
        lines=file.readlines()
        new_lines=[]

        for line in lines:
            new_lines.append(line.replace(oldstring,newstring))
    with open(filename, 'w') as file:
        for line in new_lines:
            file.write(line)


def remove_file(filename):
    if not os.path.exists(filename):
        print("An error occured")
        return

    os.remove(filename)

# alternativno try:except za gore

while line!="End":
    command,file_name,*args=line.split("-")
    if command=="Create":
        create_file(file_name)
    elif command=="Add":
        content=args[0]
        append_line_to_file(file_name,content)
    elif command=="Replace":
        old_string= args[0]
        new_string = args[1]
        replace_string_in_file(file_name,old_string,new_string)
    elif command=="Delete":
        remove_file(file_name)
    line=input()

    # Вход примерен:
    # Delete-file3.txt
    # Create-file2.txt
    # Delete-file2.txt
    # Replace-file2.txt- First- 1st
    # Add-file2.txt- New Line