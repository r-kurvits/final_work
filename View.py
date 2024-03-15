from tkinter import *
from tkinter import ttk
import tkinter.font as font


class View(Tk):
    def __init__(self, controller, model):
        super().__init__()
        self.__controller = controller
        self.__model = model
        self.__default = font.Font(family='Verdana', size=12)

        self.__width = 600
        self.__height = 300
        self.title("Lõputöö")

        self.center(self, self.__width, self.__height)
        self.__frame_top, self.__frame_bottom = self.create_frames()

        (self.__search_lbl,
         self.__open_file_lbl,
         self.__filename_lbl,
         self.__row_count_lbl,
         self.__count_lbl,
         self.__error_lbl
         ) = self.create_labels()

        self.__search_input = Entry(self.__frame_top, font=self.__default)
        self.__search_input['state'] = 'disabled'
        self.__search_input.grid(row=0, column=1, padx=5, pady=2, sticky=EW)

        self.__btn_search, self.__btn_open = self.create_buttons()

        self.bind('<Return>', lambda event: self.__controller.search_value())

    @property
    def search_input(self):
        return self.__search_input

    @property
    def lbl_filename(self):
        return self.__filename_lbl

    @property
    def lbl_count(self):
        return self.__count_lbl

    @property
    def btn_search(self):
        return self.__btn_search

    @property
    def error_lbl(self):
        return self.__error_lbl

    def main(self):
        self.mainloop()

    @staticmethod
    def center(win, w, h):
        x = int((win.winfo_screenwidth() / 2) - (w / 2))
        y = int((win.winfo_screenheight() / 2) - (h / 2))
        win.geometry(f'{w}x{h}+{x}+{y}')

    def create_frames(self):
        top = Frame(self, height=50)
        bottom = Frame(self)

        top.pack(fill=BOTH)
        bottom.pack(expand=YES, fill=BOTH)

        return top, bottom

    def create_buttons(self):
        search = Button(
            self.__frame_top,
            text='Otsi',
            font=self.__default,
            state='disabled',
            command=self.__controller.search_value
        )
        open_btn = Button(self.__frame_top, text='Ava fail', font=self.__default, command=self.__controller.open_file)

        search.grid(row=0, column=2, padx=5, pady=5, sticky=EW)

        open_btn.grid(row=0, column=3, padx=5, pady=5, sticky=EW)

        return search, open_btn

    def create_labels(self):
        search_lbl = Label(
            self.__frame_top,
            text='Sisesta otsing',
            anchor='w',
            font=self.__default
        )
        search_lbl.grid(row=0, column=0, padx=5, pady=2, sticky=EW)

        open_file_lbl = Label(
            self.__frame_top,
            text='Avatud fail:',
            anchor='w',
            font=self.__default
        )
        open_file_lbl.grid(row=1, column=0, padx=5, pady=2, sticky=EW)
        file_name_lbl = Label(
            self.__frame_top,
            text='Fail pole valitud',
            anchor='w',
            font=self.__default
        )
        file_name_lbl.grid(row=1, column=1, padx=5, pady=2, sticky=EW)

        row_count_lbl = Label(
            self.__frame_top,
            text='Ridu kokku:',
            anchor='w',
            font=self.__default
        )
        row_count_lbl.grid(row=1, column=2, padx=5, pady=2, sticky=EW)

        count_lbl = Label(
            self.__frame_top,
            text='0',
            anchor='w',
            font=self.__default
        )
        count_lbl.grid(row=1, column=3, padx=5, pady=2, sticky=EW)

        error_lbl = Label(
            self.__frame_top,
            text='',
            anchor='w',
            font=self.__default
        )
        error_lbl.grid(row=2, column=0, padx=5, pady=2, columnspan=4, sticky=EW)
        return search_lbl, open_file_lbl, file_name_lbl, row_count_lbl, count_lbl, error_lbl

    def draw_search_result(self, header, data):
        if len(data) > 0:
            table = ttk.Treeview(self.__frame_bottom)
            vsb = ttk.Scrollbar(self.__frame_bottom, orient=VERTICAL, command=table.yview)
            vsb.pack(side=RIGHT, fill=Y)
            table.configure(yscrollcommand=vsb.set)
            table.heading('#0', text='', anchor=CENTER)
            table.column('#0', anchor=CENTER, width=2)
            column_ids = [h.lower() for h in header]
            table['columns'] = column_ids
            for h in header:
                table.heading(f'{h.lower()}', text=h, anchor=CENTER)
                table.column(f'{h.lower()}', anchor=CENTER, width=50)

            x = 0
            for d in data:
                table.insert(
                    parent='',
                    index=END,
                    iid=str(x),
                    text='',
                    values=d
                )
                x += 1
            table.pack(expand=True, fill=BOTH)

    def clear_search_result(self):
        # Destroy all widgets in __frame_bottom
        for widget in self.__frame_bottom.winfo_children():
            widget.destroy()
