# import os
# import argparse
#
# def get_filenames():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-f', '--folder', required=True, help = 'Name of the folder to be sorted')
#     args = parser.parse_args()
#     file_names = []
#     for file in os.listdir(args.folder):
#         if os.path.isfile(os.path.join(args.folder, file)):
#             file_names.append(file)
#     return file_names, args.folder
#
# def ext_names(file_names):
#     file_extention_names = []
#     for name in file_names:
#         exten = os.path.splitext(name)[1]
#         if exten not in file_extention_names:
#             file_extention_names.append(exten.strip('.'))
#     print(file_extention_names)
#     print(set(file_extention_names))
#     return set(file_extention_names)
#
#
# def mkdir(extentions, location):
#     for name in extentions:
#         os.mkdir(f'{location}+{name}')
#
#
#
#
#
# def main():
#     f_list, path = get_filenames()
#     ext_list = ext_names(f_list)
#     dir_list = mkdir(ext_list, path)
#
#
# main()


a = [1,2, 3,4]

print(a[-3:])