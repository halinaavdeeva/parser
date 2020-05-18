from src.file_handler import FileHandler
from src.connection import Connection
from src.model import Model


def main():
    folder = FileHandler()
    folder.create_folder()
    folder.move_file()
    for file in folder.fb2_books(folder.path_input):
        Connection().for_main(Model(folder.path_input, file))


if __name__ == "__main__":
    main()
