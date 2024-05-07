'''
Module that provides a function that opens a text editor.
'''
# Gioele Amendola
# 02/05/2024

# Create a simple text editor that allows the user to open, edit, and save text files.
# Implement basic functionality such as inserting, deleting, and copying text.
# Provide undo/redo functionality to allow users to reverse actions.
# Save the edited text to a file when the user chooses to save.

# Import tk module for graphic user interface (gui)
from tkinter import *
from tkinter.filedialog import *
from pathlib import Path

file_name: str = "Untitled"
curr_path = Path(__file__).parent.resolve()

def initialize_texteditor():
    '''
    Initialization of gui window and its functions.
    '''

    def new_file(*args):
        '''Creates new file for insertion of text.'''
        # If pressed yes
        def process_command():
            global file_name
            textarea.delete('1.0', END)
            window.title(f"{file_name} - Text Editor")
            file_name = "Untitled"
            ask_window.destroy()
        # Creation of another window for confirmation
        ask_window = Tk()
        ask_window.title("New File")
        ask_window.geometry("300x100")
        vertical_frame = Frame(ask_window)
        vertical_frame.pack()
        Label(vertical_frame, text="Are you sure?").pack(pady=10)
        horizontal_frame = Frame(vertical_frame)
        horizontal_frame.pack(side=TOP)
        Button(horizontal_frame, name="choose1", text="Yes!", command=process_command).pack(side=LEFT)
        Button(horizontal_frame, name="choose2", text="No", command=ask_window.destroy).pack(side=LEFT)

    def open_file(*args):
        '''Open an existing file'''
        global file_name
        global curr_path
        file_path = askopenfilename(title="Select a file",
                                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            curr_path = Path(file_path).parent.resolve()
            file_name = Path(file_path).stem
            with open(str(file_path), "r", encoding="utf8") as file:
                file_text = file.read()
                textarea.delete('1.0', END)
                textarea.insert(END, file_text)
                window.title(f"{file_name} - Text Editor")

    def save_file(*args):
        '''Save file with current name'''
        # If pressed yes
        def process_command():
            global file_name
            global curr_path
            with open(str(curr_path)+"/"+file_name+".txt", 'w', encoding="utf8") as file:
                text_content = textarea.get("1.0", END)
                file.write(text_content)
                lbl["text"] = f"File Saved Correctly!\n{str(curr_path)+'/'+file_name}"
                horizontal_frame.destroy()
                Button(vertical_frame, text="Ok!",
                       command=ask_window.destroy).pack()
        # Creation of another window for confirmation
        ask_window = Tk()
        ask_window.title("Save File")
        ask_window.geometry("500x100")
        vertical_frame = Frame(ask_window)
        vertical_frame.pack()
        lbl = Label(vertical_frame, text="Are you sure?")
        lbl.pack(pady=10)
        horizontal_frame = Frame(vertical_frame)
        horizontal_frame.pack(side=TOP)
        Button(horizontal_frame, name="choose1", text="Yes!",
               command=process_command).pack(side=LEFT)
        Button(horizontal_frame, name="choose2", text="No",
               command=ask_window.destroy).pack(side=LEFT)

    def saveas_file(*args):
        '''Save file with another name'''
        global file_name
        global curr_path
        file_path = asksaveasfilename(confirmoverwrite=TRUE,
                                      defaultextension=".txt",
                                      filetypes=[("Text files","*.txt"),("All files","*.*")])
        if file_path:
            curr_path = Path(file_path).parent.resolve()
            file_name = Path(file_path).stem
            with open(str(curr_path)+"/"+file_name+".txt", 'w', encoding="utf8") as file:
                text_content = textarea.get("1.0", "end-1c")
                file.write(text_content)
                confirmation_window = Tk()
                confirmation_window.title("Confirm")
                confirmation_window.geometry("500x100")
                Label(confirmation_window,text=f"File Saved Correctly!\n{str(curr_path)+'/'+file_name}.txt").pack()
                Button(confirmation_window, text="Ok!",
                       command=confirmation_window.destroy).pack()
                window.title(f"{file_name} - Text Editor")

    def undo(*args):
        '''Undo command for text editing'''
        try:
            textarea.clipboard_clear()
            textarea.edit_undo()
        except (TypeError,TclError) as e:
            print(str(e))


    def redo(*args):
        '''Redo command for text editing'''
        try:
            textarea.clipboard_clear()
            textarea.edit_redo()
        except (TypeError,TclError) as e:
            print(str(e))

    def select_all(*args):
        '''Select all command for text editing'''
        textarea.tag_add(SEL,"0.0",END)

    def helpme():
        '''Shows every command in a new window'''

    def about():
        '''Shows info about the program'''
    # Creation of window
    window = Tk()
    window.title(f"{file_name} - Text Editor")
    # Creation of top menu bar
    menubar = Menu(window)
    # Creation of file functions
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", underline=0, accelerator="Ctrl+N", command=new_file)
    filemenu.add_separator()
    filemenu.add_command(label="Open", underline=0, accelerator="Ctrl+O", command=open_file)
    filemenu.add_command(label="Save", underline=0, accelerator="Ctrl+S", command=save_file)
    filemenu.add_command(label="Save As...", command=saveas_file)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=window.quit)
    # Creation of edit functions
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", accelerator="Ctrl+Z", command=undo)
    editmenu.add_command(label="Redo", accelerator="Ctrl+Y", command=redo)
    editmenu.add_separator()
    editmenu.add_command(label="Select All", underline=7, accelerator="Ctrl+Shift+A", command=select_all)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: Widget.event_generate("<<Cut>>"))
    editmenu.add_command(label="Copy", underline=0, accelerator="Ctrl+C", command=lambda: Widget.event_generate("<<Copy>>"))
    editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: Widget.event_generate("<<Paste>>"))
    # Creation of help functions
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=helpme)
    helpmenu.add_command(label="About...", command=about)
    # Addition of menus on menu bar
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # Creation of text space
    textarea = Text(window, wrap='word', undo=TRUE)
    textarea.pack(expand=1, fill="both")
    # Keyboard shortcuts (in case of CaseLock active)
    textarea.bind("<Control-o>",open_file)
    textarea.bind("<Control-O>",open_file)
    textarea.bind("<Control-n>",new_file)
    textarea.bind("<Control-N>",new_file)
    textarea.bind("<Control-s>",save_file)
    textarea.bind("<Control-S>",save_file)
    textarea.bind("<Control-z>",undo)
    textarea.bind("<Control-Z>",undo)
    textarea.bind("<Control-y>",redo)
    textarea.bind("<Control-Y>",redo)
    textarea.bind("<Control-Shift-z>",redo)
    textarea.bind("<Control-Shift-Z>",redo)
    textarea.bind("<Control-Shift-a>",select_all)
    textarea.bind("<Control-Shift-A>",select_all)
    # Open window
    window.config(menu=menubar)
    window.geometry("1000x800")
    window.mainloop()


# Test Example:
initialize_texteditor()
