import os

from Model import Model
from View import View
from tkinter import filedialog as fd


class Controller:
    def __init__(self):
        self.__model = Model()
        self.__view = View(self, self.__model)

    def main(self):
        self.__view.main()

    def open_file(self):
        filepath = fd.askopenfilename()
        if filepath:
            filename = os.path.basename(filepath)
            self.__view.clear_search_result()
            self.__view.lbl_count['text'] = 0
            self.__view.error_lbl['text'] = ''
            self.__view.search_input['state'] = 'normal'
            self.__view.btn_search['state'] = 'normal'
            self.__view.lbl_filename['text'] = filename
            self.__model.filename = filepath

    def search_value(self):
        search_string = self.__view.search_input.get().strip()
        if len(search_string) >= 3:
            header = self.__model.read_header()
            data = self.__model.search_data(search_string, self.__model.read_file())
            count = len(data)
            if count > 0:
                self.__view.search_input.delete(0, 'end')
                self.__view.error_lbl['text'] = ''
                self.__view.lbl_count['text'] = count
                self.__view.clear_search_result()
                self.__view.draw_search_result(header, data)
            else:
                self.__view.search_input.delete(0, 'end')
                self.__view.lbl_count['text'] = 0
                self.__view.clear_search_result()
                self.__view.error_lbl['text'] = 'Tulemusi ei leitud'
        else:
            self.__view.search_input.delete(0, 'end')
            self.__view.lbl_count['text'] = 0
            self.__view.clear_search_result()
            self.__view.error_lbl['text'] = 'Palun sisesta 3 või rohkem märki'
