Author: Allen Garza
Date: 2/24/2021

README
send2server.py and Sender.py

**********USAGE AND PREREQUISITES*********************
send2server.py can be called with the following usage in mind...

Usage: send2server.py [input_dir] [output_dir]

such that...

input_dir: Is a directory whose file structure looks like...

-input_dir
--dir_containing_imgs (aka envelope)
--dir_containing_imgs
  .
  .
  . (inside each dir_containing_imgs) (aka within each envelope)
---separate_imgs_by_filetype_dir (ext: tif, tif_master, 1500x-tospot, etc.)

and...

output_dir: Has a distinctly similar directory hierarchy to input_dir.

*********************Notes********************************

As of now, this program is reliant on the fact that the user knows and can vouch for a similar hierarchy of files b/t the input_dir
and ouput_dir. It does check this and will stop in several places if there are discrepencies.

Could also use Sender.py as its own script as well, or in conjuction with other scripts.

Future Considerations: 
- Using recursion to map directories, allowing for a bit more flexibility. 
- Having the program create output directories, so its not dependent on if the output necesarrily matches the input.
- Could fool around with different methods of copying files to optimize speed.

******************Order of Operations***********************

-send2server.py calls Sender.py using input_dir and output_dir as a part of its construction.

-Sender: can be split into two main methods: dir_setter(), and check_and_load_files()

    1.) dir_setter() - Grabs all input file paths, maps them to envelope numbers. Does the same with output paths with a similar process.
    Obtain a list of envelope numbers, we will us this as our keys.
    
    2.) check_and_load_files() - We move files by envelope number, which we have a list of obtained via dir_setter(). Using these envelope numbers as
    keys on our dictionarys where we mapped these keys to paths, paths that tell us where the files are and where the files should go.
    shutil.copyfile() does the actual copying, one file at a time.





