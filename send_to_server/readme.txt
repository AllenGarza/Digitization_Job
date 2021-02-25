send2server.py and Sender.py README

Author: Allen Garza
Date: 2/24/2021


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

output_dir: Similar to input_dir.

**************************************************************

As of now, this program is reliant on the fact that the user knows and can vouch for a similar hierarchy of files b/t the input_dir
and ouput_dir. It does check this and will stop in several places if there are discrepencies.

Future Considerations: 
- Using recursion to map directories, allowing for a bit more flexibility. 
- Having the program create output directories, so its not dependent on if the output necesarrily matches the input.

******************Order of Operations***********************

-send2server.py calls Sender.py using input_dir and output_dir as a part of its construction.

-Sender: can be split into two main methods: dir_setter(), and check_and_load_files()
    1.) dir_setter() - Grabs all input file paths, maps them to envelope numbers. Does the same with output paths.
    2.) check_and_load_files() - Using a mapper, we move files by envelope number, using envelope number as a key to obtain paths to where the files are to where the files
    need to be.





