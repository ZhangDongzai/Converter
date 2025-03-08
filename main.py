VERSION = (0, 1)


import tkinter as tk
import tkinter.filedialog
from pydub import AudioSegment


def choose_file(entry: tk.Entry) -> None:
    path = tkinter.filedialog.askopenfilename(title="选择文件",
                                              filetypes=[("wav", ".wav")])
    if path == "": return
    entry.delete(0, tk.END)
    entry.insert(0, path)


def convert(entry: tk.Entry) -> None:
    path = entry.get()
    if path == "": return
    audio = AudioSegment.from_file(path, format="wav")
    audio.export(path[0:-4] + ".flac", format="flac")


def main() -> None:
    window = tk.Tk()
    window.title("音频格式转换器 wav to flac")
    window.geometry("500x100")

    frame = tk.Frame()

    file_name_entry = tk.Entry(master=frame, width=50)
    file_choose_button = tk.Button(master=frame, text="选择文件",
                                   command=lambda: choose_file(file_name_entry))
    convert_button = tk.Button(master=frame, text="转换", 
                               command=lambda: convert(file_name_entry))
    
    frame.pack(anchor="center", padx=10, pady=10)
    file_name_entry.grid(column=0, row=0)
    file_choose_button.grid(column=1, row=0)
    convert_button.grid(column=0, row=1, columnspan=2)

    window.mainloop()


if __name__ == "__main__":
    main()
