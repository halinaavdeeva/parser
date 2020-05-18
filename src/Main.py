from src.parser.Folder import Folder
from src.model.Connection import Connection
from src.model.data_book import Model


def main():
    folder = Folder()
    folder.create_folder()
    folder.move_file()

    for file in folder.find_all_fb2_books(folder.path_input):
        if file.endswith(".fb2"):
            Connection().for_main(Model(folder.path_input, file))


if __name__ == "__main__":
    main()
