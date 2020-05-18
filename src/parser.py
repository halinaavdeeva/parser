import xml.etree.ElementTree as ET
import re
import os
import logging

logging.basicConfig(filename="../sample.log", level=logging.INFO)


class Parser:

    def __init__(self, path, file):
        self.root = ET.parse(os.path.join(path, file))

    def book_name(self):
        book_name = self.root.find(".//*[@info-type='src-book-title']").text
        logging.info('Getting statistics for {} book'.format(book_name))
        return book_name

    def number_of_paragraph(self):
        paragraphs = self.root.findall('.//{*}p')
        logging.info('Number of paragraph: {}'.format(str(len(paragraphs))))
        return len(paragraphs)

    def number_of_words(self):
        linecount = 0
        for paragraph in self.root.findall('.//{*}body'):
            full_string = re.sub(r'\W+', " ", ''.join(paragraph.itertext()))
            words_in_paragraph = re.findall(r'\b[a-zA-Z]\w*|\b[а-яА-Я]\w*', full_string)
            linecount += len(words_in_paragraph)
        logging.info('Number of words: {}'.format(str(linecount)))
        return linecount

    def number_of_letters(self):
        linecount = 0
        for paragraph in self.root.findall('.//{*}body'):
            full_string = re.sub(r'\W+', " ", ''.join(paragraph.itertext()))
            words_in_paragraph = re.findall(r'[a-zA-Z]|[а-яА-Я]', full_string)
            linecount += len(words_in_paragraph)
        logging.info('Number of letters: {}'.format(str(linecount)))
        return linecount

    def words_with_capital_letters(self):
        linecount = 0
        for paragraph in self.root.findall('.//{*}body'):
            full_string = re.sub(r'\W+', " ", ''.join(paragraph.itertext()))
            words_with_capital_letters = re.findall(r'\b[A-Z]\w*\b|\b[А-Я]\w*\b', full_string)
            linecount += len(words_with_capital_letters)
        logging.info('Number of words with capital letters: {}'.format(str(linecount)))
        return linecount

    def words_in_lowercase(self):
        linecount = 0
        for paragraph in self.root.findall('.//{*}body'):
            full_string = re.sub(r'\W+', " ", ''.join(paragraph.itertext()))
            words_in_lowercase = re.findall(r'\b[a-z]\w*|\b[а-я]\w*', full_string)
            linecount += len(words_in_lowercase)
        logging.info('Number of words in lowercase: {}'.format(str(linecount)))
        return linecount

    def second_table(self):
        logging.info("Getting statistics for the second table...")
        words = []
        paragraphs = self.root.findall('.//{*}body')

        for paragraph in paragraphs:
            full_string = ""
            string = ''.join(paragraph.itertext())
            full_string = full_string + " " + string

        full_string = re.sub(r'\W+', " ", full_string)

        split_string_in_lowercase = full_string.lower().split()
        unique_split_string_in_lowercase = set(split_string_in_lowercase)
        string_with_uppercase = re.findall(r'\b[A-Z]\w*\b|\b[А-Я]\w*\b', full_string)
        split_upper_string_in_lowercase = ' '.join(string_with_uppercase).lower().split()
        unique_split_upper_string_in_lowercase = set(split_upper_string_in_lowercase)

        for word in unique_split_string_in_lowercase:
            count_uppercase = 0
            count = split_string_in_lowercase.count(word)

            for word1 in unique_split_upper_string_in_lowercase:
                if word1 == word:
                    count_uppercase = split_upper_string_in_lowercase.count(word1)
            words.append((word, count, count_uppercase))
        return words
