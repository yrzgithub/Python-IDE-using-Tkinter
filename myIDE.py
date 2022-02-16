from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

file_path = ""


def run():
    if file_path == "":
        save_as()
    command = f"python {file_path}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    code_output.insert(1.0, output)
    code_output.insert(1.0, error)


def save():
    with open(file_path, "w") as f:
        code = editor.get(1.0, END)
        f.write(code)


def save_as():
    global file_path
    if file_path == "":
        file_path = asksaveasfilename(filetypes=[("python files", "*.py")])
    with open(file_path, "w") as f:
        code = editor.get(1.0, END)
        f.write(code)


def open_file():
    global file_path
    file_path = askopenfilename(filetypes=[("python files", "*.py")])
    with open(file_path, "r") as f:
        code = f.read()
        editor.delete(1.0, END)
        editor.replace(1.0, END, code)


compiler = Tk()
compiler.title("YRZ IDE")
editor = Text()

menu_bar = Menu(compiler)
menu_for_files = Menu(menu_bar, tearoff=0)
menu_for_files.add_command(label="Open", command=open_file)
menu_for_files.add_command(label="Save", command=save)
menu_for_files.add_command(label="Save As", command=save_as)
menu_for_files.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=menu_for_files)
menu_bar.add_command(label="Run", command=run)
compiler.configure(menu=menu_bar)
editor.pack()
code_output = Text(height=5)
code_output.pack()
compiler.mainloop()
