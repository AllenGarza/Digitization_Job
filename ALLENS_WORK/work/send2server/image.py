import re


class Image:

    def __init__(self, image, extension):

        self.image = image
        self.file_extension = extension
        self.pattern = None
        self.year = None
        self.envelope_num = None
        self.image_num = None
        self.set_info()


    def set_info(self):
        self.pattern = re.compile("^([A-Z]+)(_)(\d+)(-)(\d)(_)(/d+)")


        # group 3 = year
        self.year = self.pattern.groups(3)
        # group 5 = envelope_num
        self.envelope_num = self.pattern.groups(5)
        # group 7 = image_num
        self.image_num = self.pattern.groups(7)

    def get_image(self):
        return self.image

    def get_file_extension(self):
        return self.file_extension

    def get_year(self):
        return self.year

    def get_envelope_num(self):
        return self.envelope_num

    def get_image_num(self):
        return self.image_num