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
    print("SMDR_tracking_checker START. \n")
    if len(sys.argv) != 4:
        print('\nUsage: SMDR_tracking_checker.py ["tracking_dir"] ["spotted_imgs_dir"] ["tospot_imgs_dir"] \n')
        print('Be sure to place "" around your input addresses. Should the files be stored in the same directory '
              'as the tracking, then typing a full address is not necessary. \n')
        print("Outputs: '***_OUT_.xlsx' to wherever your tracking_dir is stored.")
        quit()

    if not os.path.isdir(sys.argv[2]):
        print('\nEnsure you are entering in directories correctly for ["spotted_imgs_dir"] \n')
        print('Usage: SMDR_tracking_checker.py ["tracking_dir"] ["spotted_imgs_dir"] ["tospot_imgs_dir"] \n')
        print('Be sure to place "" around your input addresses. Should the files be stored in the same directory '
              'as the tracking, then typing a full address is not necessary. \n')
        print("Outputs: '***_OUT_.xlsx' to wherever your tracking_dir is stored.")
        quit()

    if not os.path.isdir(sys.argv[3]):
        print('\nEnsure you are entering in directories correctly for ["tospot_imgs_dir"] \n')
        print('Usage: SMDR_tracking_checker.py ["tracking_dir"] ["spotted_imgs_dir"] ["tospot_imgs_dir"] \n')
        print('Be sure to place "" around your input addresses. Should the files be stored in the same directory '
              'as the tracking, then typing a full address is not necessary. \n')
        print("Outputs: '***_OUT_.xlsx' to wherever your tracking_dir is stored.")
        quit()



    # Testing #
    # tracking_dir = r'C:\Users\allen\PycharmProjects\work\file_checker\checker_env\SMDR_1961_Capture-and-Processing'
    # spotted_imgs_dir = r'C:\Users\allen\PycharmProjects\work\file_checker\checker_env\batch1\toqc'
    # tospot_imgs_dir = r'C:\Users\allen\PycharmProjects\work\file_checker\checker_env\batch1'
    # Testing #

    check = checker.Checker(sys.argv[1], sys.argv[2], sys.argv[3])
    # check = checker.Checker(tracking_dir, spotted_imgs_dir, tospot_imgs_dir)
    check.save_df()

    quit()


if __name__ == "__main__":
    main()
