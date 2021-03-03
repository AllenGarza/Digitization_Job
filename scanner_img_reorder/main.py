import os
from ReOrder import ReOrder

# plan:
''' take all images into account, 4 images => 1 scan of 2-fold,
call 1 Scan S.
S = [i1, i2, i3, i4]
s.t page numbers of: i1 - 1 = i4 and i2 + 1 = i3

Suppose we have a family of scans, call it U.
U = {S1, S2, . . . , Sn}

we can say S1 contains pages (n, 1, 2, n-1) in that order
S2 contains pages n-2, 3, 4, n-3

so. . . .

Sn contains pages n/2 + 2, n/2 - 1, n/2, n/2 + 1

This seems like a divide and conquer problem.

Base Case: we have 1 S.



If count the number of images in a directory, we can tell how many scans there are, given 1 scan is 4 images.
Once we know our scans,create a queue of them.

organize_files()
'''


def main():
    dir = r''
    reorder = ReOrder(dir)


if __name__ == '__main__':
    main()
