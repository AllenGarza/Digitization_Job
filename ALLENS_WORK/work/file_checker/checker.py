"""SMDR_tracking_checker
1/18/2020
@Author Allen Garza

This is meant to be used in conjunction with SMDR_tracking_checker.
"""

import re
import os
import pandas as pd
import openpyxl
from collections import defaultdict
import copy


class Checker:
    """Checker class, handles and processes data, saves final .xlsx

    The 'Checker' class is what holds the methods for loading the excel sheet, as well as images
    in a directory and parsing the data. We use the 'num_spotted' and 'num_tospot' columns and create our own
    columns listed as 'num_spotted_in_folder' and 'num_tospot_in_folder'. They will list how many of the images there are
    in each corresponding folder. Returns a saved ***-OUT-.xlsx wherever the directory of the original tracking sheet
    is.

    Args:
        dir_of_tracking (str): directory of where tracking sheet is.
        dir_of_spotted_imgs(str): directory of where spotted images are saved, typically '../toqc/ .
        dir_of_tospot_imgs(str): directory of where tospot images are saved.

    Attributes:
        dir_of_tracking (str): directory of where tracking sheet is.
        dir_of_spotted_imgs(str): directory of where spotted images are saved, typically '../toqc/ .
        dir_of_tospot_imgs(str): directory of where tospot images are saved.
        tracking_df(pd.Dataframe): dataframe containing our info.
        file_name(str): the base name of the file of the sheet.
        counter(float/int): a counter used for various operations.
        spotted_or_tospot(bool): a selector of the order of operations.
        
    Methods:
        load_tracking()
        load_spotted_imgs_info()
        load_tospot_imgs_info()
        save_df()
        initial_file(re.pattern)
        df_updater(int, re.pattern)
        
    """

    def __init__(self, dir_of_tracking, dir_of_spotted_imgs, dir_of_tospot_imgs):
        """Constructor that initiates everything.
        
        Directories passed as arguments allows us to access all the necessary dirs and files
        for the application of this program.
     
        """
        
        self.tracking_df = None
        self.file_name = os.path.basename(dir_of_tracking)

        self.counter = None
        self.spotted_or_tospot = False # false implies spotted, refer to load_spotted_images_info() and df_updater()

        self.dir_of_tracking = dir_of_tracking
        self.dir_of_spotted_imgs = dir_of_spotted_imgs
        self.dir_of_tospot_imgs = dir_of_tospot_imgs

        Checker.load_tracking(self)  # loads database (excel tracking sheet)
        Checker.load_spotted_imgs_info(self)  # creates df for spotted imgs info
        Checker.load_tospot_imgs_info(self)  # creates df for tospot imgs info

    def load_tracking(self): # -> dataframe
        """Loads pd.Dataframe from the tracking .xlsx sheet.

        We filter columns and rename what's left.
        A cap of 500 rows is set to improve load times, change if necessary.

        :return:
        """

        dir_of_tracking_xlsx = self.dir_of_tracking + '.xlsx'
        df = pd.read_excel(dir_of_tracking_xlsx, nrows= 500)
        df_refined = df[['Envelope Title', 'Envelope #', '# Spotted', 'ToSpot']]
        df_refined = df_refined.rename(columns={"Envelope #": "envelope_num", "# Spotted": "num_spotted"})
        self.tracking_df = df_refined
        print('tracking loaded \n')

    def load_spotted_imgs_info(self): # -> dataframe
        """Counts number of images are in a folder.

        A regex pattern is used, to ensure the files correspond to the correct
        envelope numbers, and are in fact images.

        :returns dataframe
        """

        self.spotted_or_tospot = False
        self.tracking_df['num_spotted_in_folder'] = None

        # SMDR_1961-Envelope#_XXX ## NAMING TEMPLATE ##
        pattern = re.compile("^([A-Z]+.\d+).(\d+)(.)(\d+)")  # we only care about groups 2 and 4

        # we iterate through directory containing images.
        # do character match using regex, find 2nd group of characters and 4th, containing
        # "Envelope#" and "XXX", then we parse 'Envelope#' and 'XXX' as float64, add to new dataframe

        initial_env_num = self.initial_file(pattern) # find initial file at top of list of imgs in folder using regex pattern

        self.df_updater(initial_env_num, pattern)

        print('spotted imgs loaded \n')

    def load_tospot_imgs_info(self): # -> dataframe
        """Counts number of images are in a folder.

        A regex pattern is used,to ensure the files correspond to the correct envelope numbers,
        and are in fact images.

        :returns dataframe
        """

        self.spotted_or_tospot = True
        self.tracking_df['num_ToSpot_in_folder'] = None

        # SMDR_1961-Envelope#_XXX ## NAMING TEMPLATE ##
        pattern = re.compile("^([A-Z]+.\d+).(\d+)(.)(\d+)")  # only care about groups 2 and 4

        initial_env_num = self.initial_file(pattern)

        self.df_updater(initial_env_num, pattern)

        print('to spot imgs loaded \n')

    def save_df(self): # -> .xlsx
        """saves final dataframe.

        Changes working directory to where the original tracking sheet is saved, saves new dataframe as
        ***-OUT-.xlsx file in same directory.
        :return:
        """

        d = len(os.path.basename(self.dir_of_tracking))
        save_dir = self.dir_of_tracking[:-d]
        os.chdir(save_dir)
        output_name = self.file_name[:-4] + "-OUT-.xlsx"
        self.tracking_df.to_excel(output_name)
        print('SAVED')

    # allows us to find the top of the list of imgs, letting us know what envelope number our list begins with
    def initial_file(self, pattern):
        """finds the first file to begin counting.

        We do this as, know the files will follow one another from top to bottom. We obtain the top images name and env_num,
        knowing the rest will follow.

        :param pattern: regex pattern obtained from template naming of names.
        :return:  initial_env_number
        """

        file_list = os.listdir(self.dir_of_spotted_imgs)    # list containing list of files
        self.counter = 0

        while True:
            curr_env_num = str(file_list[self.counter]) # 'XXXXXXXX.tif'
            if curr_env_num[-4:] != '.tif':    # if f is not the first image at the top of the list of imgs in dir we skip that file and restart loop
                self.counter = self.counter + 1
                continue
            m = pattern.match(curr_env_num)
            initial_env_num = float(m.group(2))  # make an "initial counter"
            return initial_env_num
            break

    def df_updater(self, curr_env_num, pattern):
        """Counts images, ensures they correspond to a specific entry, saves this information into dataframe.
        Does this sequentially, can change this to use recursion in the future sometime maybe.

        :param curr_env_num: starting envelope number.
        :param pattern: pattern of naming template.
        :return: dataframe
        """

        # recall, self.spotted_or_tospot is False
        self.counter = 0.0

        if not self.spotted_or_tospot:
            for f in os.listdir(self.dir_of_spotted_imgs):
                if f[-4:] != '.tif':    # a quick check to ensure it is the correct format '.tif'
                    continue


                imgstr = str(f)
                m = pattern.match(imgstr)
                envelope_num = float(m.group(2))
                # img_num = float(m.group(4))

                if envelope_num == curr_env_num:
                    self.counter = self.counter + 1.0
                    num = copy.deepcopy(self.counter)
                    self.tracking_df.loc[self.tracking_df['envelope_num'] == curr_env_num, ['num_spotted_in_folder']] = num
                else:
                    num = copy.deepcopy(self.counter)
                    self.tracking_df.loc[self.tracking_df['envelope_num'] == curr_env_num, ['num_spotted_in_folder']] = num
                    self.counter = 0.0
                    continue

        else: # implies we're working on ToSpot folder
            for f in os.listdir(self.dir_of_tospot_imgs):
                if f[-4:] != '.tif':    # a quick check to ensure it is the correct format '.tif'
                    continue


                imgstr = str(f)
                m = pattern.match(imgstr)
                envelope_num = float(m.group(2))
                # img_num = float(m.group(4))

                if envelope_num == curr_env_num:
                    self.counter = self.counter + 1.0
                    num = copy.deepcopy(self.counter)
                    self.tracking_df.loc[self.tracking_df['envelope_num'] == curr_env_num, ['num_ToSpot_in_folder']] = num
                else:
                    num = copy.deepcopy(self.counter)
                    self.tracking_df.loc[self.tracking_df['envelope_num'] == curr_env_num, ['num_ToSpot_in_folder']] = num
                    self.counter = 0.0
                    continue





