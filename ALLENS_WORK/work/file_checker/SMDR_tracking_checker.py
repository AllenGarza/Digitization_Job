"""SMDR_tracking_checker
1/18/2021
@Author Allen Garza

This program will compare an SMDR tracking sheet with its
corresponding 'spotted images' and 'tospot images' folders
to ensure the all images are accounted for.

"""

import os
import sys
import checker
import pandas as pd


def main():
    if len(sys.argv) != 4:
        print('Usage: SMDR_tracking_checker.py [tracking_dir] [spotted_imgs_dir] [tospot_imgs_dir] \n')
        print("Outputs: '***_OUT_.xlsx' to wherever your tracking_dir is stored.")

    # Testing #
    # tracking_dir = r'C:\Users\allen\PycharmProjects\work\file_checker\checker_env\SMDR_1961_Capture-and-Processing'
    # spotted_imgs_dir = r'C:\Users\allen\PycharmProjects\work\file_checker\checker_env\batch1\toqc'
    # tospot_imgs_dir = r'C:\Users\allen\PycharmProjects\work\file_checker\checker_env\batch1'
    # Testing #

    check = checker(sys.argv[1], sys.argv[2], sys.argv[3])
    # check = checker.Checker(tracking_dir, spotted_imgs_dir, tospot_imgs_dir)
    check.save_df()

    quit()


if __name__ == "__main__":
    main()
