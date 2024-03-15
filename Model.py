import csv


class Model:
    def __init__(self):
        self.__filename = None
        self.__line = 0
        self.__header = []
        self.__data = []

    @property
    def filename(self):
        return self.__filename

    @property
    def header(self):
        return self.__header

    @property
    def data(self):
        return self.__data

    @filename.setter
    def filename(self, value):
        self.__filename = value

    def read_header(self):
        self.__header = []
        with open(self.__filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            try:
                self.__header = next(reader)
            except StopIteration:
                pass
            file.seek(0)
        return self.__header

    def read_file(self):
        self.__data = []
        with open(self.__filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                self.__data.append(row)
            file.seek(0)
        return self.__data

    def search_data(self, search_string, data):
        search_results = []
        for row in data:
            for item in row:
                if search_string.lower() in item.lower():
                    search_results.append(row)
                    break
        return search_results
