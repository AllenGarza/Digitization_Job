import os
import sys
import re
from multipledispatch import dispatch
import image
from collections import defaultdict
from shutil import copyfile

class Sender:

    '''
    during construction, our sender checks and loads files

    finds the pattern (list of patterns can be added to, consider creating
    an abstract class to make this easier(?) to modify).
    '''

    def __init__(self, *args):

        if len(args) == 4: # mixed_files (subject to change based on project)
            self.input_jpg_dir = None
            self.input_tif_dir = None
            self.input_dir = None
            self.output_dir = None
            self.input_dir_setter(*args)

            self.files_tif, self.files_jpg = None, None
            self.pattern = None
            self.counter = 0
            self.tif_size = 0
            self.jpg_size = 0

            self.p1 = None #should initialize these here.
            self.p2 = None
            self.p3 = None

            self.choose_pattern()
            self.file_divider_jpg = {} # key should match value of image.output_dir, value is actual output
            self.file_divider_tif = {}
            self.files_jpg, self.files_tif = self.check_and_load_files_scrambled() # loads all images in
            self.file_divider_setter() # sets up our output_dir dictionary
            self.order_files() # assigns the imgs in self.files_jpg and *_tif to the respective dirs.


        elif len(args) == 4:
            self.input_dir_tif, self.input_dir_jpg = self.input_checker_parser(args[1], args[2])

    '''Categorize files into two vectors, one of tifs, other of jpgs, obtain file size of each vector as well
    in tif_size and jpg_size.
    
    '''
    @dispatch(str, str)
    def input_dir_setter(self, dir_1, dir_2): # the case where only 1 input and 1 output are given.

        if not os.path.isdir(dir_1) or not os.path.isdir(dir_2):
            print("please input correct directories,")
            exit()

    @dispatch(str, str, str)
    def input_dir_setter(self, dir_1, dir_2, dir_3): # the case where we have 2 inputs and on output.

        if not os.path.isdir(dir_1) or not os.path.isdir(dir_2) or not os.path.isdir(dir_3):
            print("please input correct directories,")
            exit()

        dir_1 = str(dir_1)
        dir_2 = str(dir_2)
        dir_3 = str(dir_3)

        list_of_dir = [dir_1, dir_2, dir_3]
        for x in list_of_dir:
            if 'tif' in x:
                self.input_dir_tif = x
                list_of_dir.remove(x)
            elif 'jpg' in x:
                self.input_dir_jpg = x
                list_of_dir.remove(x)
            else:
                self.output_dir = x
                list_of_dir.remove(x)
        print("here's your directories . . . .\n")
        print(self.input_dir_jpg)
        print(self.input_dir_tif)
        print(self.output_dir)

    @property
    def check_and_load_files_scrambled(self):
        files_tif = []
        files_jpg = []
        file_list = os.listdir(self.input_dir)

        for f in self.files_tif:
            f_name = str(f)
            if (f_name[:-4]) == '.tif':
                img = image(f, 'tif')
                files_tif.append(img)
                self.output_dir[img] = img.get_output_dir()
                self.tif_size = self.tif_size + os.stat(f).st_size  # in bytes


        for f in self.files_jpg:
            f_name = str(f)
            if (f_name[:-4]) == 'jpg':
                img = image(f, 'jpg')
                files_jpg.append(img)
                self.output_dir[img] = img.get_output_dir()
                self.jpg_size = self.jpg_size + os.stat(f).st_size  # in bytes


        self.tif_size = self.tif_size * (10 ^ (-6))  # b to MB
        self.jpg_size = self.jpg_size * (10 ^ (-6))  # b to MB
        return files_tif, files_jpg

    @property
    def choose_pattern(self):
        # SMDR_1961-Envelope                             ## NAMING TEMPLATE ##
        self.p1 = re.compile("^([A-Z]+)(_)(\d+)(-)(\d)")
        # self.p3 = re.compile("")
        # .
        # .
        # .
        # pn

        file_name = str(self.files_tif[0])

        if re.match(self.p1, file_name):
            return self.p1
        elif re.match(self.p2, file_name):
            return self.p2
        # elif re.match(pn, file_name):

    def file_divider_setter(self):
        if self.pattern == self.p1:
            print("Checking Output Folder. . ." + self.output_dir + '\n')
            if os.path.isdir(self.output_dir):
                output_dir_list = os.listdir(self.output_dir)
                for dir in output_dir_list:

                    envelope = os.path.basename(os.path.normpath(dir))  # gets base path.
                    self.file_divider_tif[envelope] = []
                    self.file_divider_jpg[envelope] = []

        # elif self.pattern == self.p2:

    def prompt_copy(self):
        assert isinstance(self.output_dir, object)
        assert isinstance(self.input_dir, object)
        total = self.jpg_size + self.tif_size

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

    '''we are gonna create vectors, where each vector is a group of img sorted by their envelope number
    then we will assign an output to it via dictionary key/value pairs. our key is our output directory containing the
    directories of images by their env num. assigned to each key is a list containing all images that are meant to go into 
    their corresponding folders.
    '''
    def order_files(self):

        for img in self.files_tif:  # refer to image.py class
            envelope_dir = img.get_output_dir()
            if envelope_dir in self.file_divider:
                self.file_divider[envelope_dir].append(img)


    def copy_files(self):

        copy = self.prompt_copy()

        if copy:
            print("...MOVING FILES...")
            for dir in os.listdir(self.output_dir):
                dir_name = str(os.path.basename(dir))
                tif_or_jpg_dirs = os.listdir(dir)
                for tif_or_jpg_dir in tif_or_jpg_dirs:
                    os.chdir(tif_or_jpg_dir)
                    tif_or_jpg = str(os.path.basename(tif_or_jpg_dir))
                    if tif_or_jpg == 'tif':
                        output = os.path.join(dir, tif_or_jpg_dir, tif_or_jpg)
                        os.path.

                    if dir_name in self.file_divider:
                        batch = self.file_divider[dir_name]  # vector containing our images.
                        os.write()

