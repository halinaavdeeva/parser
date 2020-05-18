from src.Parser import Parser


class Model:
    def __init__(self, path, file):
        info = Parser(path, file)
        self.book_name = info.book_name()
        self.number_of_paragraphs = info.number_of_paragraph()
        self.number_of_words = info.number_of_words()
        self.number_of_letters = info.number_of_letters()
        self.words_with_capital_letters = info.words_with_capital_letters()
        self.words_in_lowercase = info.words_in_lowercase()
        self.second_table = info.second_table()

    def get_table(self):
        return [self.book_name,
                self.number_of_paragraphs,
                self.number_of_words,
                self.number_of_letters,
                self.words_with_capital_letters,
                self.words_in_lowercase]

    def get_second_table(self):
        return [self.book_name, self.second_table]
