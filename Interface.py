__author__ = 'root'

from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
import tarfile

from LocalisationFr import LocalisationFr


class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(LocalisationFr.WINDOW_PROGRAM_NAME.value)
        self.panel_about = self.panel_about()
        self.panel_pollute = self.panel_pollute()
        self.panel_unpollute = self.panel_unpollute()
        self.menu()
        self.resizable(width=FALSE, height=FALSE)
        self.show_panel_pollute()

    def menu(self):
        menubar = Menu(self, tearoff=0)
        menubar.add_command(label=LocalisationFr.PANEL_POLLUTE.value, command=self.show_panel_pollute)
        menubar.add_command(label=LocalisationFr.PANEL_UNPOLLUTE.value, command=self.show_panel_unpollute)
        menubar.add_command(label=LocalisationFr.PANEL_ABOUT.value, command=self.show_panel_about)

        self.config(menu=menubar)

    def show_panel_pollute(self):
        self.panel_pollute.pack()
        self.panel_unpollute.pack_forget()
        self.panel_about.pack_forget()

    def show_panel_unpollute(self):
        self.panel_pollute.pack_forget()
        self.panel_unpollute.pack()
        self.panel_about.pack_forget()

    def show_panel_about(self):
        self.panel_unpollute.pack_forget()
        self.panel_pollute.pack_forget()
        self.panel_about.pack()

    def panel_about(self):
        panel_about = PanedWindow(self, orient=HORIZONTAL)
        p_file_name = PanedWindow(panel_about, orient=HORIZONTAL)
        p_file_name.add(Label(p_file_name, text=LocalisationFr.PANEL_ABOUT_CONTENT.value))
        p_file_name.pack(side=TOP, fill=BOTH, padx=5)
        return panel_about

    def panel_pollute(self):
        panel_pollute = PanedWindow(self, orient=HORIZONTAL)
        p_file_name = PanedWindow(panel_pollute, orient=HORIZONTAL)
        p_file_name.add(Label(p_file_name, text=LocalisationFr.PANEL_POLLUTE_CONTENT.value))
        p_file_name.pack(side=TOP, fill=BOTH, padx=5)

        self.pollute_input_file_path = Entry(p_file_name, textvariable=StringVar(), width=50)
        p_file_name.add(self.pollute_input_file_path)
        p_file_name.add(Button(panel_pollute, text=LocalisationFr.TEXT_BROWSE.value, command=self.load_directory))
        p_file_name.pack(side=TOP, fill=BOTH, padx=5)

        Button(panel_pollute, text=LocalisationFr.PANEL_POLLUTE_BUTTON.value, command=self.lauch_pollute()).pack(
            padx=10, pady=10)
        return panel_pollute

    def panel_unpollute(self):
        panel_unpollute = PanedWindow(self, orient=HORIZONTAL)
        p_file_name = PanedWindow(panel_unpollute, orient=HORIZONTAL)
        p_file_name.add(Label(p_file_name, text=LocalisationFr.PANEL_UNPOLLUTE_CONTENT.value))
        p_file_name.pack(side=TOP, fill=BOTH, padx=5)

        self.unpollute_input_file_path = Entry(p_file_name, textvariable=StringVar(), width=50)
        p_file_name.add(self.unpollute_input_file_path)
        p_file_name.add(Button(panel_unpollute, text=LocalisationFr.TEXT_BROWSE.value, command=self.load_directory))
        p_file_name.pack(side=TOP, fill=BOTH, padx=5)

        Button(panel_unpollute, text=LocalisationFr.PANEL_UNPOLLUTE_BUTTON.value, command=self.lauch_pollute()).pack(
            padx=10, pady=10)
        return panel_unpollute

    def load_directory(self):
        fname = askdirectory()
        if fname:
            try:
                self.pollute_input_file_path.delete(0, 10000)
                self.pollute_input_file_path.insert(0, fname)
                self.unpollute_input_file_path.delete(0, 10000)
                self.unpollute_input_file_path.insert(0, fname)
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)

    def lauch_pollute(self):
        test ="t"

    def lauch_unpollute(self):
        test ="t"

