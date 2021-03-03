import os


class ReOrder:
    def __init__(self, directory):
        self.working_dir = directory
        self.files_by_name = []
        self.files_by_scan = {}
        self.file_page_map = {}
        self.index_0 = 0
        self.index_n = 0
        self.read_in_files(directory)
        self.organize_in_dict()
        self.reorder()

    def read_in_files(self, directory):
        list_files = os.listdir(self.working_dir)
        counter = 0
        scan = 0
        names = []
        for file in list_files:
            if 'tif' in str(file) or 'jpg' in str(file):
                counter = counter + 1
                name = str(file)
                names.append(name)
                self.files_by_name.append(name)
                if counter == 4:
                    self.files_by_scan[scan] = names.copy()  # scan associated with images
                    scan = scan + 1  # num of scans
                    counter = 0
                    names.clear()

        files = self.files_by_name
        self.index_n = len(files) - 1  # nth file in files_by_name

    def organize_in_dict(self):
        for scan in self.files_by_scan:
            images = self.files_by_scan[scan]

            self.file_page_map[images[0]] = self.index_n
            self.file_page_map[images[1]] = self.index_0
            self.file_page_map[images[2]] = self.index_0 + 1
            self.file_page_map[images[3]] = self.index_n - 1

            self.index_0 = self.index_0 + 2
            self.index_n = self.index_n - 2

    def reorder(self):
        os.chdir(self.working_dir)

        for file in self.files_by_name:
            page_num = str(self.file_page_map[file])
            new_file_name = file[:-7]
            new_file_name = new_file_name + page_num.zfill(4) + '.tif'
            dir_of_file = os.path.join(self.working_dir, file)
            dir_of_renamed_file = os.path.join(self.working_dir, new_file_name)
            os.rename(dir_of_file, dir_of_renamed_file)
