import tkinter as tk
from tkinter import ttk

from File import File
from Sector import Sector

class StorageSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Storage Simulator")
        self.geometry("800x400")

        self.file_entries = []
        self.sectors = []

        self.create_widgets()

    def create_widgets(self):
        self.file_name_label = ttk.Label(self, text="File Name:")
        self.file_name_label.grid(column=0, row=0)

        self.file_name_entry = ttk.Entry(self)
        self.file_name_entry.grid(column=1, row=0)

        self.file_size_label = ttk.Label(self, text="File Size:")
        self.file_size_label.grid(column=2, row=0)

        self.file_size_entry = ttk.Entry(self)
        self.file_size_entry.grid(column=3, row=0)

        self.hidden_var = tk.BooleanVar()
        self.hidden_check = ttk.Checkbutton(self, text="Hidden", variable=self.hidden_var)
        self.hidden_check.grid(column=4, row=0)

        self.read_only_var = tk.BooleanVar()
        self.read_only_check = ttk.Checkbutton(self, text="Read Only", variable=self.read_only_var)
        self.read_only_check.grid(column=5, row=0)

        self.add_button = ttk.Button(self, text="Add", command=self.add_file)
        self.add_button.grid(column=6, row=0)

        self.remove_button = ttk.Button(self, text="Remove", command=self.remove_file)
        self.remove_button.grid(column=7, row=0)

        self.file_info_table = ttk.Treeview(self, columns=("name", "size", "hidden", "read_only"), show="headings")
        self.file_info_table.heading("name", text="File Name")
        self.file_info_table.heading("size", text="File Size")
        self.file_info_table.heading("hidden", text="Hidden")
        self.file_info_table.heading("read_only", text="Read Only")
        self.file_info_table.grid(column=0, row=1, columnspan=8)

    def add_file(self):
        name = self.file_name_entry.get()
        size = int(self.file_size_entry.get())
        hidden = self.hidden_var.get()
        read_only = self.read_only_var.get()

        new_file = File(name, size, hidden, read_only)
        self.file_entries.append(new_file)

        size_left = size
        prev_sector = None

        while size_left > 0:
            sector = Sector(prev_sector=prev_sector)
            if prev_sector is not None:
                prev_sector.next_sector = sector

            self.sectors.append(sector)
            prev_sector = sector
            size_left -= len(sector.data)

        self.file_info_table.insert("", "end", values=(name, size, hidden, read_only))

    def remove_file(self):
        selected_item = self.file_info_table.selection()[0]
        selected_index = self.file_info_table.index(selected_item)
        selected_file = self.file_entries[selected_index]

        size_left = selected_file.size

        while size_left > 0:
            sector = self.sectors.pop(0)
            size_left -= len(sector.data)

        self.file_info_table.delete(selected_item)
        self.file_entries.pop(selected_index)