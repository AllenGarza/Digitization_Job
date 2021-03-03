Author: Allen F. Garza
Date: 3/3/2021

README
ReOrder.py

****************************What it does*********************************
The following script reorders 2-fold scans of any particular document scanned by the
Fujitsu machine. Projects such as hillviews are an example of where it could be used.

The script assumes the the pattern of images follows through out the directory, and that
sets of images are already categorized. 

One idea is to use this script in conjuction with the
'directory_creator_by_file.py' script, that groups files by their file names.

Changes data INPLACE.

**************************Environment****************************************
The directory 'env' is provided to emulate a use-case of the code. To test. . .

1.) Open main in notepad or IDE
2.) Place the full address of the directory (diR) you want to change in og_dir = r'diR'
3.) Run main()

I'd recommend taking note of the files in the env, before running, or creating a copy, as it will
change these files in place.