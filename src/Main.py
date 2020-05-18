from src.file_work.file_handler import FileHandler
from src.model.Connection import Connection
from src.model.data_book import Model


def main():
    folder = FileHandler()
    folder.create_folder()
    folder.move_file()
    for file in folder.find_all_fb2_books(folder.path_input):
        if file.endswith(".fb2"):
            Connection().for_main(Model(folder.path_input, file))


if __name__ == "__main__":
    main()
