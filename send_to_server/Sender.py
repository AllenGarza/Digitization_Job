import os
import sys
import re
from multipledispatch import dispatch
import image
from collections import defaultdict
from shutil import copyfile  # we'll use copy2


class Sender:
    '''
    during construction, our sender checks and loads files

    finds the pattern (list of patterns can be added to, consider creating
    an abstract class to make this easier(?) to modify).
    '''

    def __init__(self, *args):

        self.input_dir = None
        self.output_dir = None

        self.counter = 0
        self.file_size = 0

        self.envelopes = []  # list containing titles of envelopes, will use as keys later in file_divider
        self.file_paths = []
        self.file_divider = {}  # key should match value of image.output_dir, value is actual output
        self.file_mapper = {}
        self.files = None

        self.dir_setter(*args)
        self.file_divider_setter()  # sets up our output_dir dictionary
        self.order_files()  # assigns the imgs in self.files_jpg and *_tif to the respective dirs.

    '''Categorize files into two vectors, one of tifs, other of jpgs, obtain file size of each vector as well
    in tif_size and jpg_size.
    
    '''

    @dispatch(str, str)
    def dir_setter(self, input_dir, output_dir):  # the case where only 1 input and 1 output are given.

        if not os.path.isdir(input_dir):
            print("ERROR: Input Directory is not a true directory.")
            exit()
        elif not os.path.isdir(output_dir):
            print("ERROR: Output Directory is not a true directory.")
        else:
            dirs_containing_imgs = os.listdir(input_dir)  # a list containing all of our 'envelopes'
            dirs_to_contain_imgs = os.listdir(output_dir)  # output list containing all of our 'envelopes'
            for dir in dirs_containing_imgs:  # each dir containing images
                envelope = str(os.path.basename(dir))  # get basename of dir (envelope)
                self.envelopes.append(envelope)  # append to our list of envelopes
                self.file_divider[envelope] = []  # use key and associate an empty list
                dir_path = os.path.join(input_dir, dir)  # get path of the envelope
                file_extensions = os.listdir(
                    dir_path)  # get names directories that show a separation by file type (tif, jpg) within envelope
                for file_extension in file_extensions:  # for each directory that separates imgs by file type
                    self.file_divider[envelope].append(file_extension)  # add file types within each envelope to a
                    # list and associate list with envelopes
                    path_of_files = os.path.join(dir_path, file_extension)
                    self.file_paths = path_of_files
                    self.file_mapper[path_of_files] = None
                    self.check_and_load_files(path_of_files)

            file_type_ex = self.file_divider[self.envelopes[0]]

            print("here are the directories . . . .\n")
            print('INPUT dirs: ', dirs_to_contain_imgs, '\n')
            print('OUTPUT dirs: ', dirs_to_contain_imgs, '\n')
            print('Files are separated by:', file_type_ex)
            print('Is this correct?')

    @property
    def check_and_load_files(self, path_of_files):
        files = os.listdir(path_of_files)
        size_of_directory = 0
        for file in files:
            file_path = os.path.join(path_of_files, file)
            size_of_directory = size_of_directory + os.stat(file_path)  # in bytes

        size_of_directory = size_of_directory * 10 ^ (-6)  # in MB
        # we now know the size of files in each subdirectory of the file types.
        # lets associate the size with the address.

        self.file_mapper[
            path_of_files] = size_of_directory  # mapping the address of each group of files to values of their size.

    def prompt_copy(self):
        for dir_containing_imgs in self.file_paths:
            file_ext = os.path.basename(dir_containing_imgs)  # (tif, jpg, tospot, etc.)

        while "the answer is invalid.\n":
            print("Do you want to move: \n",
                  self.jpg_size, "MB of jpgs, \n",
                  self.tif_size, "MB of tifs, \n",
                  total, "MB total \n",
                  "from " + self.input_dir + " to " + self.output_dir + "?")
            reply = str(input('(y/n): ').lower().strip())
            if reply[:1] == 'y':
                return True
            elif reply[:1] == 'n':
                return False

    def copy_files(self):
        copy = self.prompt_copy()
