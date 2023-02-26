import os
import argparse

#############################################################
# Name: get_filenames
# Brief: This function parse the source directory and create a list of files in it.
# Inpits: --folder - source directory
# Outputs:
# Return: file_names - list of files in source directory
#         args.folder - full path of source directory
#############################################################

def get_filenames():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', required=True, help = 'Name of the folder to be sorted')
    args = parser.parse_args()
    file_names = []
    for file in os.listdir(args.folder):
        if os.path.isfile(os.path.join(args.folder, file)):
            file_names.append(file)
    return file_names, args.folder


#############################################################
# Name: ext_names
# Brief: This function iterates over all files in directory and create a 'set' of extensions
# Inpits: file_names - list of files
# Outputs:
# Return: file_extention_names - set of all file extantions in source directory
#############################################################

def ext_names(file_names):
    file_extention_names = []
    for name in file_names:
        exten = os.path.splitext(name)[1]
        file_extention_names.append(exten)
    return set(file_extention_names)


#############################################################
# Name: mkdir
# Brief: This function create new folders in our source directory by names in file_extention_names
# Inpits: extentions - set of file extentions
#         location - source folder
# Outputs: In source directory wil be created new folders
# Return:
#############################################################

def mkdir(extentions, location):
    dirs = []
    for name in extentions:
        if not os.path.exists(f'{location}Folder{name}'):
            os.mkdir(f'{location}Folder{name}')
            dirs.append(f'{location}Folder{name}')
    for dir in os.listdir(location):
        if os.path.isdir(os.path.join(location, dir)):
            dirs.append(dir)

#############################################################
# Name: move_files
# Brief: This function cheks content of source directory and move files in corresponding folder
# Inpits: file_source - source folder
# Outputs: Move the files in the correct folders
# Return:
#############################################################

def move_files(file_sourse):
    for file in os.listdir(file_sourse):
        if os.path.isfile(os.path.join(file_sourse, file)):
            os.replace(file_sourse+file, file_sourse+'Folder'+os.path.splitext(file)[1]+'/'+file)



def main():
    f_list, path = get_filenames()
    ext_list = ext_names(f_list)
    mkdir(ext_list, path)
    move_files(path)
    print(os.system(f'tree {path}'))

main()
