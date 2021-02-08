import os
import sys
import re
from multipledispatch import dispatch
import image
from collections import defaultdict

class Sender:

    '''during construction, our sender checks and loads files

    finds the pattern (list of patterns can be added to, consider creating
    an abstract class to make this easier(?) to modify).




    '''

    def __init__(self, *args):

        if len(args) == 4: # mixed_files (subject to change based on project)
            self.input_jpg_dir = None
            self.input_tif_dir = None
            self.input_dir = None
            self.output_dir = None
            self.dir_setter(*args)

            self.files_tif, self.files_jpg
            self.pattern
            self.counter = 0
            self.tif_size = 0
            self.jpg_size = 0

            self.p1 = None
            self.p2 = None
            self.p3 = None

            self.choose_pattern()
            self.files_jpg, self.files_tif = self.check_and_load_files_scrambled()

        elif len(args) == 4:
            self.input_dir_tif, self.input_dir_jpg = self.input_checker_parser(args[1], args[2])

    '''Categorize files into two vectors, one of tifs, other of jpgs, obtain file size of each vector as well
    in tif_size and jpg_size.
    
    '''
    @dispatch(str, str)
    def dir_setter(self, dir_1, dir_2): # the case where only 1 input and 1 output are given.

        if not os.path.isdir(dir_1) or not os.path.isdir(dir_2):
            print("please input correct directories,")
            exit()

    @dispatch(str, str, str)
    def dir_setter(self, dir_1, dir_2, dir_3): # the case where we have 2 inputs and on output.

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

        for f in file_list:

            f_name = str(f)
            if (f_name[:-4]) == '.tif':
                img = image(f, 'tif')
                files_tif.append(img)
                self.tif_size = self.tif_size + os.stat(f).st_size  # in bytes
            elif (f_name[:-4]) == 'jpg':
                img = image(f, 'jpg')
                files_jpg.append(img)
                self.jpg_size = self.jpg_size + os.stat(f).st_size  # in bytes

            self.counter = self.counter + 1
        self.tif_size = self.tif_size * (10 ^ (-6))  # b to MB
        self.jpg_size = self.jpg_size * (10 ^ (-6))  # b to MB
        return files_tif, files_jpg

    @property
    def choose_pattern(self):
        # SMDR_1961-Envelope#_XXX ## NAMING TEMPLATE ##
        self.p1 = re.compile("^([A-Z]+)(_)(\d+)(-)(\d)")
        # self.p3 = re.compile("")
        # .
        # .
        # .
        # pn

        file_name = str(self.files_jpg[0])

        if re.match(self.p1, file_name):
            return self.p1
        elif re.match(self.p2, file_name):
            return self.p2
        # elif re.match(pn, file_name):

    def check_output(self):
        if self.pattern == self.p1:
            print("Checking Output Folder: " + self.output_dir + '\n')
            if os.path.isdir(self.output_dir):
                output_dir_list = os.listdir(self.output_dir)
                for dir in output_dir_list:
                    if dir != 'tif' and dir != 'jpg':
                        return False
                return True
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

    def move_files(self):
        pass
