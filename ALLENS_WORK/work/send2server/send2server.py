import os
import sys
import Sender


def main():
    global sender

    if len(sys.argv) < 4:
        print('MIXED_FILES Usage: send2server.py [input_dir] [output_dir] \n')
        print('SMDR Usage: send2server.py [input_dir_tif] [input_dir_jpg] [output_dir] \n')
        print('Copies files by string into corresponding file extension folders in output_dir \n')
        exit()

    if sys.argv == 3:
        sender = Sender(sys.argv[1], sys.argv[2])
    elif sys.argv == 4:
        sender = Sender(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main()
