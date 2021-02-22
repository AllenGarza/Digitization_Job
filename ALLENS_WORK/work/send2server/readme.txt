send2server.py and Sender.py README

Author: Allen Garza
Date: 2/11/2021


**********USAGE AND PREREQUISITES************
send2server.py can be called with the following usage in mind...
Usage: send2server.py [input_dir] [output_dir]

# input_dir: A directory whose file structure looks like. . .

-input_dir
--dir_containing_imgs
--dir_containing_imgs
  .
  .
  . (inside each dir_containing_imgs)
---separate_imgs_by_filetype (ex.tif, 1_tif, 1500x-tospot, etc.) # NOTE: Images may be separated by an arbitrary amount of file types.

# output_dir: Similar to input_dir.
***************************************

As of now, this program is reliant on the fact that the user knows and can vouch for a similar hierarchy of files b/t the input_dir
and ouput_dir.

******************Order of Operations***********************

-send2server.py calls Sender.py using input_dir and output_dir as a part of its construction.

-Sender.py then calls dir_setter() using our input_dir and output_dir as parameters, and takes 
note of all of the dirs_containing_imgs within input_dir, as well as their separation by file type.
A dictionary is used to correlate the envelope the images are in and the types of file extensions,
within the envelope. A prompt asks if everything is correct so far.

-


creating a dictionary whose key is the 

