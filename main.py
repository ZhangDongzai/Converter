VERSION = (0, 2)


import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment


def choose_file(entry: tk.Entry) -> None:
    path = askopenfilename(title="选择文件", filetypes=[(('music file'),
                           ('.wav', '.flac', '.mp3', '.aac', '.wma',
                            '.ogg', '.ape', '.dsf', '.dff'))])
    if path == "": return
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, path)
    entry.config(state="readonly")


def convert(entry: tk.Entry, combobox: ttk.Combobox) -> None:
    path = entry.get()
    print(path)
    for i in range(1, 6):
        if path[-i] == ".":
            audio = AudioSegment.from_file(path, format=path[-i+1:])
            audio.export(path[0:-i] + combobox.get(), format=combobox.get()[1:])


def main() -> None:
    window = tk.Tk()
    window.title("音频文件转换器")
    window.geometry("500x100")

    frame = tk.Frame()

    file_name_entry = tk.Entry(master=frame, width=50, state="readonly")
    file_choose_button = tk.Button(master=frame, text="选择文件",
                                   command=lambda: choose_file(file_name_entry))
    convert_combobox = ttk.Combobox(master=frame, values=('.wav', '.flac',
                                    '.mp3', '.aac', '.wma', '.ogg', '.ape',
                                    '.dsf', '.dff'), state="readonly")
    convert_button = tk.Button(master=frame, text="转换", 
                               command=lambda: convert(file_name_entry,
                                                       convert_combobox))
    
    frame.pack(anchor="center", padx=10, pady=10)
    file_name_entry.grid(column=0, row=0)
    file_choose_button.grid(column=1, row=0)
    convert_combobox.grid(column=0, row=1)
    convert_button.grid(column=1, row=1)

    window.mainloop()


if __name__ == "__main__":
    main()
