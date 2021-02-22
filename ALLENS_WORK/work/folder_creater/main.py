import os
import sys
from shutil import copyfile

# a quick script which creates folders with housing similarly named files. Assumes files are ordered.
# copies files, works best if used on local drive

def main():
    dir = r'C:\00_DigitalImaging\Hillviews\batch_8-perfect_bound' # dir containing files we want to categorize
    os.chdir(dir)   # changing working directory
    files = os.listdir(dir) # list of all files in the dir
    first = None
    for file in files:
        if os.path.isdir(file): # if the file is a directory then we skip until we find the first file.
            continue
        else:
            first = str(file[:-9]) # once first file is found, we take its name with the intention of creating a new dir
            break

    os.mkdir(first) # new dir, named after first file found
    new_dir = os.path.join(dir, first)
    os.chdir(new_dir)

    folder_of_imgs = []
    imgs_mapper = {}

    name = first

''' we will iterate through our files, ensure it is an .tif file, and ensure it is similar named.
If similarly named we add it to our list, and copy it over to its respective directory. Else, we will
create a new directory and place it in there, then continue having moved on to a new directory.
'''
    for file in files:
        if os.path.isdir(file):
            break
        if name in str(file) and '.tif' in str(file):
            folder_of_imgs.append(file)
            dir_of_file = os.path.join(dir, file)
            new_dir_of_file = os.path.join(new_dir, file)

            copyfile(dir_of_file, new_dir_of_file)
        else:
            os.chdir(dir)

            imgs_mapper[name] = folder_of_imgs.copy()

            name = str(file)[:-9]
            os.mkdir(name)
            new_dir = os.path.join(dir, name)
            os.chdir(new_dir)
            folder_of_imgs = []

            folder_of_imgs.append(file)
            dir_of_file = os.path.join(dir, file)
            new_dir_of_file = os.path.join(new_dir, file)

            copyfile(dir_of_file, new_dir_of_file)


if __name__ == '__main__':
    main()
