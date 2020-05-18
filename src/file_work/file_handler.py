import os
import shutil
import logging


logging.basicConfig(filename="../sample.log", level=logging.INFO)


class FileHandler:
    def __init__(self):
        self.path_input = ""
        self.path_incorrect_input = ""

    def create_folder(self):
        page = os.path.expanduser('~')
        self.path_input = os.path.join(page, 'Desktop', 'input')
        self.path_incorrect_input = os.path.join(page, 'Desktop', 'incorrect_input')

        try:
            if not os.path.isdir(self.path_input):
                os.mkdir(os.path.join(page, 'Desktop', 'input'))
            if not os.path.isdir(self.path_incorrect_input):
                os.mkdir(self.path_incorrect_input)
                logging.info("Input and Incorrect input folders were created")
        except OSError as error:
            logging.error("Creation of the folder failed", error)

    def move_file(self):
        for file in os.listdir(self.path_input):
            if not file.endswith(".fb2"):
                logging.info("File {} was moved to {}".format(os.path.join(self.path_input,
                                                                           file), self.path_incorrect_input))
                shutil.move(os.path.join(self.path_input, file), self.path_incorrect_input)

    def find_all_fb2_books(self, path):
        list_of_files = []
        for file in os.listdir(path):
            if file.endswith(".fb2"):
                logging.info("Processing of file {} in progress...".format(os.path.join(path, file)))
                list_of_files.append(file)

        return list_of_files
