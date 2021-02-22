import os
import sys
import re

# a quick script for renaming exported hillviews in D:\Hillviews_exports\tif\

def main():
    og_dir = r'D:\Hillviews_exports\tif\Batch-2' # change accordingly.
    hillview_dirs = os.listdir(og_dir)
    for dir in hillview_dirs:
        name = str(os.path.basename(dir)) # takes base name ex: Hillviews_1993-Spring
        images = os.listdir(os.path.join(og_dir, dir)) # lists images in each Hillviews folder.
        counter = 1
        for img in images:
            num = str(counter) # ith image
            num = "_" + num.zfill(4) + ".tif" # adds _, padded leading 0, and .tif; _000i.tif
            name_number = name + num # basename added; Hillviews_1993-Spring_000i.tif
            img_dir = os.path.join(dir, img) # creates a direct path to the image
            os.chdir(os.path.join(og_dir, dir)) # changes working directory to working envelope num;
                                                # Hillviews_1993-Spring dir
            os.rename(img, name_number) # does final renaming of image file in envelope dir.
            counter = counter + 1 # iterate counter.


if __name__ == '__main__':
    main()
