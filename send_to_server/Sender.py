import os
from multipledispatch import dispatch
from shutil import copyfile


class Sender:
    def __init__(self, *args):
        self.file_size = 0

        self.file_paths = []
        self.envelopes_in = []
        self.envelopes_out = []
        self.envelopes_mapped_to_extension = []
        self.envelope_mapped_to_paths = dict()
        self.file_divider_input = dict()
        self.file_divider_output = dict()
        self.files = None

        self.dir_setter(*args)
        self.check_and_load_files()

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

            for dir in dirs_containing_imgs:  # each dir containing extensions dirs
                envelope = str(os.path.basename(dir))  # get basename of dir (envelope)
                self.file_divider_input[envelope] = set()
                self.envelopes_in.append(envelope)  # append to our list of envelopes, will use them as keys
                dir_path = os.path.join(input_dir, dir)  # get path of the envelope
                file_extensions = os.listdir(dir_path)  # separation by file type (tif, jpg) within envelope
                for file_extension in file_extensions:  # for each directory that separates images by file type
                    file_extension_path = os.path.join(dir_path, file_extension)
                    self.file_divider_input[envelope].add(file_extension_path) # envelope maps to path of files by extension

            for dir in dirs_to_contain_imgs:
                envelope = str(os.path.basename(dir))
                self.file_divider_output[envelope] = set()
                self.envelopes_out.append(envelope)
                envelope_output_dir = os.path.join(output_dir, dir)
                file_extensions = os.listdir(envelope_output_dir)
                for file_extension in file_extensions:
                    out_file_extension_path = os.path.join(envelope_output_dir, file_extension)
                    self.file_divider_output[envelope].add(out_file_extension_path)

            print("here are our files by envelope . . . .\n")
            print('INPUT: ', dirs_to_contain_imgs, '\n')
            print('OUTPUT: ', dirs_to_contain_imgs, '\n')
            print('Is this correct?')
            # place prompt here, then begin transfer, check_and_load_files() called in __init__

    # the following assums all directories are created and matched.
    # should probably consider the case where directories aren't already established
    def check_and_load_files(self):
        for envelope in self.envelopes_in:
            assert envelope in self.envelopes_out
            file_extension_paths_input = list(self.file_divider_input[envelope])
            file_extension_paths_output = list(self.file_divider_output[envelope])

            num_of_extensions = len(self.file_divider_input[envelope])
            assert num_of_extensions == len(self.file_divider_output[envelope])

            for x in range(num_of_extensions):
                file_path_in = file_extension_paths_input.pop()
                file_path_out = file_extension_paths_output.pop()
                files = os.listdir(file_path_in)
                for file in files:
                    file_path_in_specific = os.path.join(file_path_in, file)
                    file_path_out_specific = os.path.join(file_path_out, file)
                    copyfile(file_path_in_specific, file_path_out_specific)

 # not yet implimented ########
    def prompt_copy(self):
        total = 0
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


