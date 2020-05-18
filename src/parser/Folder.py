import os
import shutil
import logging


logging.basicConfig(filename="../sample.log", level=logging.INFO)


class Folder:
    def __init__(self):
        self.path_input = ""
        self.path_incorrect_input = ""

    def create_folder(self):
        home = os.path.expanduser('~')
        self.path_input = os.path.join(home, 'Documents', 'books', 'input')
        self.path_incorrect_input = os.path.join(home, 'Documents', 'books', 'incorrect_input')

        try:
            if not os.path.isdir(os.path.join(home, 'Documents', 'books')):
                os.mkdir(os.path.join(home, 'Documents', 'books'))
            if not os.path.isdir(self.path_input):
                os.mkdir(os.path.join(home, 'Documents', 'books', 'input'))
                logging.info("Input folder was created")
            if not os.path.isdir(self.path_incorrect_input):
                os.mkdir(self.path_incorrect_input)
        except OSError as error:
            logging.error("Creation of the directory failed")

    def move_file(self):
        for file in os.listdir(self.path_input):
            if not file.endswith(".fb2"):
                logging.info("File {} was moved to {}".format(os.path.join(self.path_input,
                                                                           file), self.path_incorrect_input))
                try:
                    shutil.move(os.path.join(self.path_input, file), self.path_incorrect_input)
                except:
                    logging.error(
                        "File {} already exists in directory {}".format(file, self.path_incorrect_input))

    def find_all_fb2_books(self, path):
        list_of_files = []
        for file in os.listdir(path):
            if file.endswith(".fb2"):
                logging.info("Processing of file {} in progress...".format(os.path.join(path, file)))
                list_of_files.append(file)

        return list_of_files
