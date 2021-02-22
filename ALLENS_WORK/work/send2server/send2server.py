import os
import sys
from Sender import Sender


def main():
    # global sender

    # if len(sys.argv) != 3:
    #    print('Usage: send2server.py [input_dir] [output_dir] \n')

    # elif sys.argv == 3:
    #    sender = Sender(sys.argv[1], sys.argv[2])

    input_dir_test = r'C:\Users\afg38\Desktop\code\send2server\env\data'
    output_dir_test = r'C:\Users\afg38\Desktop\code\send2server\env\smdr\SMDR'
    sender = Sender(input_dir_test, output_dir_test)


if __name__ == '__main__':
    main()
