#! /usr/bin/env python3
#-*- conding utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from src_gui.my_dict import Dict

class MyDialogGif:

    def __init__(self, parent):

        self.top = Toplevel(parent)
        self.top.grab_set()
        self.top.title("Make your GIF")

        self.all_types = [("All Files", ".*"), ("JPEG",".jpg .jpeg"),
            ("PNG", ".png"),("BMP", ".bmp"), ("GIF", ".gif")]
        self.img_list = None
        self.path = None
        self.duration = 100
        self.loop_mode = 0
        self.evt = None
        self.all_files = Dict()

        self.can_but = Canvas(self.top)

        self.can_img = Canvas(self.can_but, width=150, height=150, bg="white")
        self.but_add = Button(self.can_but, text="Add Picture(s) to selection",
                                command=self.add_files)
        self.lab_dur = Label(self.can_but, text="Duration of each frame\n(milliseconds) :")
        self.ent_dur = Entry(self.can_but, width=5)
        self.lab_loop = Label(self.can_but, text="Number of loop\n (0 = infinite) :")
        self.ent_loop = Entry(self.can_but, width=5)
        self.but_up = Button(self.can_but, text="Up", command=self.up)
        self.but_down = Button(self.can_but, text="Down", command=self.down)
        self.but_del = Button(self.can_but, text="Delete", command=self.delete)
        self.but_save = Button(self.can_but, text="Save GIF", command=self.save)
        self.but_cancel = Button(self.can_but, text="Cancel", command=self.top.destroy)

        self.ent_dur.insert(0, str(self.duration))
        self.ent_loop.insert(0, str(self.loop_mode))

        self.can_img.grid(column=1, row=0, padx=5, pady=5, columnspan=2)
        self.but_add.grid(column=1, row=1, padx=5, pady=10, columnspan=2)
        self.lab_dur.grid(column=1, row=2, pady=5, sticky="E")
        self.ent_dur.grid(column=2, row=2, padx=10, pady=5, sticky="W")
        self.lab_loop.grid(column=1, row=3, pady=5, sticky="E")
        self.ent_loop.grid(column=2, row=3, padx=10, pady=5, sticky="W")
        self.but_up.grid(column=1, row=4, padx=10, pady=5, sticky="W")
        self.but_down.grid(column=1, row=4, padx=5, pady=5, columnspan=2)
        self.but_del.grid(column=2, row=4, padx=5, pady=5)
        self.but_save.grid(column=1, row=5, padx=5, pady=5, sticky="N")
        self.but_cancel.grid(column=2, row=5, padx=5, pady=5, sticky="N")

        self.can_but.grid(column=3, row=1, sticky="NS", padx=5, pady=5)


        self.yscroll = ttk.Scrollbar(self.top, orient=VERTICAL)
        self.yscroll.grid(column=2, row=1, sticky="NS")

        self.res_box = Listbox(self.top, width=50, height=23, selectmode="single",
                                yscrollcommand=self.yscroll.set)
        self.res_box.grid(column=1, row=1, padx=10, pady=10)

        self.yscroll.config(command=self.res_box.yview)

        self.res_box.bind('<<ListboxSelect>>', self.selection)

    def add_files(self):

        files = self.path = filedialog.askopenfilenames(filetype=self.all_types)

        for file in files:
            img = Image.open(file)
            name = os.path.basename(file)
            self.all_files[name] = img
            self.res_box.insert("end", name)


    def save(self):

        try:
            self.duration = int(self.ent_dur.get())
            self.loop_mode = int(self.ent_loop.get())

        except ValueError:
            messagebox.showerror("Error", "A number is expected")

        else:
            self.path = filedialog.asksaveasfilename(filetype=[("GIF", ".gif")])

            if self.path:
                self.img_list = self.all_files.lvalues()
                self.top.destroy()

    def up(self):

        res, index = self.get_act()

        if res is None:
            return

        try:
            self.all_files.swap(index, index - 1)
            self.res_box.delete(index)
            self.res_box.insert(index - 1, res)
            self.res_box.selection_set(index - 1)

        except IndexError:
            pass

    def down(self):

        res, index = self.get_act()

        if res is None:
            return

        try:
            self.all_files.swap(index, index + 1)
            self.res_box.delete(index)
            self.res_box.insert(index + 1, res)
            self.res_box.selection_set(index + 1)

        except IndexError:
            pass

    def delete(self):

        res, index = self.get_act()

        if res is None:
            return

        self.res_box.delete(index)
        del self.all_files[res]

    def get_act(self):
        try:
            w = self.evt.widget
            index = int(w.curselection()[0])
            return w.get(index), index

        except IndexError:
            return None, None

        except AttributeError:
            return None, None

    def selection(self, evt):

        self.evt = evt
        res, index = self.get_act()

        if res is None:
            return

        selected = self.all_files[res]
        selected = selected.resize((150,150), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(selected)
        self.can_img.create_image(0, 0, image=img, anchor=NW)
        self.can_img.image = img

    def get_res(self):

        return self.img_list, self.path, self.duration, self.loop_mode


if __name__ == '__main__':

    root = Tk()
    d = MyDialogGif(root)
    root.wait_window(d.top)
