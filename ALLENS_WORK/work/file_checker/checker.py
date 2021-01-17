import re
import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import openpyxl
import numpy as np
from collections import defaultdict


class Checker:

    def __init__(self, dir_of_tracking, dir_of_spotted_imgs, dir_of_tospot_imgs):
        self.tracking_df = None
        self.spotted_imgs_df = None
        self.tospot_imgs_df = None

        self.dir_of_tracking = dir_of_tracking
        self.dir_of_spotted_imgs = dir_of_spotted_imgs
        self.dir_of_tospot_imgs = dir_of_tospot_imgs

        Checker.load_tracking(self)  # loads database (excel tracking sheet)
        Checker.load_spotted_imgs_info(self)  # creates df for spotted imgs info
        Checker.load_tospot_imgs_info(self)  # creates df for tospot imgs info
        Checker.compare_dfs(self)

        print(dir_of_tracking.head())

    def load_tracking(self):
        dir_of_tracking_xlsx = self.dir_of_tracking + '.xlsx'
        df = pd.read_excel(dir_of_tracking_xlsx)
        df_refined = df[['Envelope #', '# Spotted', 'ToSpot']]
        df_refined = df_refined.rename(columns={"Envelope #": "envelope_num", "# Spotted": "num_spotted"})
        self.tracking_df = df_refined

    def load_spotted_imgs_info(self):
        spotted_imgs_df = self.tracking_df
        spotted_imgs_df['num_spotted_in_folder'] = float(0)

        # SMDR_1961-Envelope#_XXX ## NAMING TEMPLATE ##
        pattern = re.compile("^([A-Z]+.\d+).(\d+)(.)(\d+)")  # we only care about groups 2 and 4

        # we iterate through directory containing images.
        # do character match using regex, find 2nd group of characters and 4th, containing
        # "Envelope#" and "XXX", then we parse 'Envelope#' and 'XXX' as float64, add to new dataframe

        initial_env_num = self.initial_file(pattern) # find inital file at top of list of imgs in folder using regex pattern

        self.spotted_imgs_df = self.df_updater(spotted_imgs_df, initial_env_num, pattern)


    def load_tospot_imgs_info(self):
        tospot_imgs_df = pd.DataFrame(columns=['envelope_num', 'ToSpot_in_folder'], dtype=float)

        # SMDR_1961-Envelope#_XXX ## NAMING TEMPLATE ##
        pattern = re.compile("^([A-Z]+.\d+).(\d+)(.)(\d+)")  # only care about groups 2 and 4

        envelope_num_master = None
        for f in os.listdir(self.dir_of_tospot_imgs):
            if f[-4:] == ".tif" or ".jpg":
                imgstr = str(f)
                m = pattern.match(imgstr)
                envelope_num = float(m.group(2))
                img_num = float(m.group(4))
                if spotted_imgs_df[spotted_imgs_df.iloc[:, ]]
                spotted_imgs_df = tospot_imgs_df.append({'envelope_num': envelope_num, 'ToSpot_in_folder': img_num}, ignore_index=True)

        self.tospot_imgs_df = tospot_imgs_df

    def compare_dfs(self): #    RE-EVALUATE #####################
        # We now have 3 different dfs.
        # We will merge and compare them to find any potential discrepancies

        tracking_df = self.tracking_df
        spotted_df = self.spotted_imgs_df
        tospot_imgs_df = self.tospot_imgs_df

        tracking_df

        pass


    # allows us to find the top of the list of imgs, letting us know what envelope number our list begins with
    def initial_file(self, pattern):
        file_list = os.listdir(self.dir_of_spotted_imgs)    # list containing list of files
        f = -1      # counter

        while True:
            f = f + 1
            curr_env_num = str(file_list[f])
            if f[:-4] != '.tif':    # if f is not the first image at the top of the list of imgs in dir we skip that file and restart loop
                continue
            m = pattern.match(curr_env_num)
            initial_env_num = float(m.group(2))  # make an "initial counter"
            return initial_env_num
            break

    def df_updater(self, df, curr_env_num, pattern):

        for f in os.listdir(self.dir_of_spotted_imgs):
            if f[:-4] != '.tif':    # a quick check to ensure it is the correct format '.tif'
                continue

            
            imgstr = str(f)
            m = pattern.match(imgstr)
            envelope_num = float(m.group(2))
            # img_num = float(m.group(4))

            if envelope_num == curr_env_num:


            else


            specific_row = df.loc[df.envelope_num == envelope_num]

            return spotted_imgs_df





