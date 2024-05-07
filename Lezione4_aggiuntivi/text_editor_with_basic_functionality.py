'''
Module that provides a function that opens a text editor.
'''
# Gioele Amendola
# 05/05/2024

# Create a simple text editor that allows the user to open, edit, and save text files.
# Implement basic functionality such as inserting, deleting, and copying text.
# Provide undo/redo functionality to allow users to reverse actions.
# Save the edited text to a file when the user chooses to save.

# Import tk module for graphic user interface (gui)
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from pathlib import Path

file_name: str = "Untitled"
curr_path = Path(__file__).parent.resolve()
file_extension: str = ".txt"

def initialize_texteditor():
    '''
    Initialization of gui window and its functions.
    '''

    def new_file(*_):
        '''Creates new file for insertion of text.'''
        # If pressed yes
        def process_command():
            global file_name
            global file_extension
            global curr_path
            textarea.delete('1.0', END)
            window.title(f"{file_name} - Text Editor")
            file_name = "Untitled"
            file_extension = ".txt"
            curr_path = Path(__file__).parent.resolve()
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
        Button(horizontal_frame,
               name="choose1",
               text="Yes!",
               command=process_command).pack(side=LEFT)
        Button(horizontal_frame,
               name="choose2",
               text="No",
               command=ask_window.destroy).pack(side=LEFT)

    def open_file(*_):
        '''Open an existing file'''
        global file_name
        global curr_path
        global file_extension
        file_path = askopenfilename(title="Select a file",
                                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            curr_path = Path(file_path).parent.resolve()
            file_name = Path(file_path).stem
            file_extension = Path(file_path).suffix
            with open(str(file_path), "r", encoding="utf8") as file:
                file_text = file.read()
                textarea.delete('1.0', END)
                textarea.insert(END, file_text)
                window.title(f"{file_name} - Text Editor")

    def save_file(*_):
        '''Save file with current name'''
        # If pressed yes
        def process_command():
            global file_name
            global curr_path
            global file_extension
            with open(str(curr_path)+"/"+file_name+file_extension, 'w', encoding="utf8") as file:
                text_content = textarea.get("1.0", "end-1c")
                file.write(text_content)
                lbl["text"] = f"File Saved Correctly!\n{str(curr_path)+'/'+file_name+file_extension}"
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

    def saveas_file(*_):
        '''Save file with another name'''
        global file_name
        global curr_path
        global file_extension
        file_path = asksaveasfilename(confirmoverwrite=TRUE,
                                      defaultextension=".txt",
                                      filetypes=[("Text files","*.txt"),("All files","*.*")])
        if file_path:
            print(file_path)
            curr_path = Path(file_path).parent.resolve()
            file_name = Path(file_path).stem
            file_extension = Path(file_path).suffix
            with open(str(curr_path)+"/"+file_name+file_extension, 'w', encoding="utf8") as file:
                text_content = textarea.get("1.0", "end-1c")
                file.write(text_content)
                confirmation_window = Tk()
                confirmation_window.title("Confirm")
                confirmation_window.geometry("500x100")
                Label(confirmation_window,
                      text="File Saved Correctly!\n"+
                      f"{str(curr_path)+'/'+file_name+file_extension}").pack()
                Button(confirmation_window, text="Ok!",
                       command=confirmation_window.destroy).pack()
                window.title(f"{file_name} - Text Editor")

    def undo(*_):
        '''Undo command for text editing'''
        try:
            textarea.clipboard_clear()
            textarea.edit_undo()
        except (TypeError,TclError) as e:
            print(str(e))

    def redo(*_):
        '''Redo command for text editing'''
        try:
            textarea.clipboard_clear()
            textarea.edit_redo()
        except (TypeError,TclError) as e:
            print(str(e))

    def select_all(*_):
        '''Select all command for text editing'''
        textarea.tag_add(SEL,"1.0",END)
        return "break"

    def paste(*_):
        '''Paste Text from clipboard'''
        text_content = textarea.clipboard_get()
        text_content = text_content.strip()
        position = textarea.index(INSERT)
        textarea.insert(position, text_content)
        return "break"

    def helpme():
        '''Shows every command in a new window'''
        helpme_window = Tk()
        helpme_window.title("All available commands")
        helpme_window.geometry("500x400")
        helpme_frame = Frame(helpme_window)
        helpme_frame.pack(fill='both')
        # Template
        name0 = Label(helpme_frame, text="Name")
        description0 = Label(helpme_frame, text="Description")
        shortcut0 = Label(helpme_frame, text="Shortcut")
        name0.grid(column=1, row=0, padx=10)
        description0.grid(column=2, row=0, padx=30)
        shortcut0.grid(column=3, row=0, padx=10)
        # File Menu
        separator0 = Separator(helpme_frame)
        separator0.grid(row=1, column=1, columnspan=100, sticky=EW)
        topic0 = Label(helpme_frame, text="File Menu:")
        topic0.grid(column=0, row=2, padx=5)
        # New
        name1 = Label(helpme_frame, text="New")
        description1 = Label(helpme_frame, text="Open New File")
        shortcut1 = Label(helpme_frame, text="Ctr+N")
        name1.grid(column=1, row=2, padx=10, pady=5)
        description1.grid(column=2, row=2, padx=30, pady=5)
        shortcut1.grid(column=3, row=2, padx=10, pady=5)
        # Open
        name2 = Label(helpme_frame, text="Open")
        description2 = Label(helpme_frame, text="Open Existing File")
        shortcut2 = Label(helpme_frame, text="Ctr+O")
        name2.grid(column=1, row=3, padx=10, pady=5)
        description2.grid(column=2, row=3, padx=30, pady=5)
        shortcut2.grid(column=3, row=3, padx=10, pady=5)
        # Save
        name3 = Label(helpme_frame, text="Save")
        description3 = Label(helpme_frame, text="Save File")
        shortcut3 = Label(helpme_frame, text="Ctr+S")
        name3.grid(column=1, row=4, padx=10, pady=5)
        description3.grid(column=2, row=4, padx=30, pady=5)
        shortcut3.grid(column=3, row=4, padx=10, pady=5)
        # Save As
        name4 = Label(helpme_frame, text="Save As")
        description4 = Label(helpme_frame, text="Save File with\nnew name and path", justify=CENTER)
        shortcut4 = Label(helpme_frame, text="")
        name4.grid(column=1, row=5, padx=10, pady=5)
        description4.grid(column=2, row=5, padx=30, pady=5)
        shortcut4.grid(column=3, row=5, padx=10, pady=5)
        # Quit
        name5 = Label(helpme_frame, text="Quit")
        description5 = Label(helpme_frame, text="Close Window")
        shortcut5 = Label(helpme_frame, text="")
        name5.grid(column=1, row=6, padx=10, pady=5)
        description5.grid(column=2, row=6, padx=30, pady=5)
        shortcut5.grid(column=3, row=6, padx=10, pady=5)
        # Edit Menu
        separator1 = Separator(helpme_frame)
        separator1.grid(row=7, column=1, columnspan=100, sticky=EW)
        topic1 = Label(helpme_frame, text="Edit Menu:")
        topic1.grid(column=0,row=8)
        # Undo
        name6 = Label(helpme_frame, text="Undo")
        description6 = Label(helpme_frame, text="Undo last action")
        shortcut6 = Label(helpme_frame, text="Ctrl+Z")
        name6.grid(column=1, row=8, padx=10, pady=5)
        description6.grid(column=2, row=8, padx=30, pady=5)
        shortcut6.grid(column=3, row=8, padx=10, pady=5)
        # Redo
        name7 = Label(helpme_frame, text="Redo")
        description7 = Label(helpme_frame, text="Redo last\nundone action", justify=CENTER)
        shortcut7 = Label(helpme_frame, text="Ctr+Y\nCtrl+Shift+Z", justify=CENTER)
        name7.grid(column=1, row=9, padx=10, pady=5)
        description7.grid(column=2, row=9, padx=30, pady=5)
        shortcut7.grid(column=3, row=9, padx=10, pady=5)
        # Select All
        name8 = Label(helpme_frame, text="Select All")
        description8 = Label(helpme_frame, text="Select all text")
        shortcut8 = Label(helpme_frame, text="Ctrl+A")
        name8.grid(column=1, row=10, padx=10, pady=5)
        description8.grid(column=2, row=10, padx=30, pady=5)
        shortcut8.grid(column=3, row=10, padx=10, pady=5)
        # Cut
        name9 = Label(helpme_frame, text="Cut")
        description9 = Label(helpme_frame, text="Cut selected text")
        shortcut9 = Label(helpme_frame, text="Ctrl+X")
        name9.grid(column=1, row=11, padx=10, pady=5)
        description9.grid(column=2, row=11, padx=30, pady=5)
        shortcut9.grid(column=3, row=11, padx=10, pady=5)
        # Copy
        name10 = Label(helpme_frame, text="Copy")
        description10 = Label(helpme_frame, text="Copy selected text")
        shortcut10 = Label(helpme_frame, text="Ctrl+C")
        name10.grid(column=1, row=12, padx=10, pady=5)
        description10.grid(column=2, row=12, padx=30, pady=5)
        shortcut10.grid(column=3, row=12, padx=10, pady=5)
        # Paste
        name11 = Label(helpme_frame, text="Paste")
        description11 = Label(helpme_frame, text="Paste copied text")
        shortcut11 = Label(helpme_frame, text="Ctrl+V")
        name11.grid(column=1, row=13, padx=10, pady=5)
        description11.grid(column=2, row=13, padx=30, pady=5)
        shortcut11.grid(column=3, row=13, padx=10, pady=5)

    def about():
        '''Shows info about the program'''
        about_window = Tk()
        about_window.title("Informations")
        about_window.geometry("250x250")
        lbl1 = Label(about_window,
                     text=" This program was created in 2 days\nby Gioele Amendola",
                     justify=CENTER)
        lbl1.place(relx=0, rely=0.33)
        lbl2 = Label(about_window, text="07/05/2024")
        lbl2.pack(side=BOTTOM)

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
    editmenu.add_command(label="Select All", underline=7, accelerator="Ctrl+Shift+A",
                         command=select_all)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", accelerator="Ctrl+X",
                         command=lambda: Widget.event_generate(window, "<Control-x>"))
    editmenu.add_command(label="Copy", underline=0, accelerator="Ctrl+C",
                         command=lambda: Widget.event_generate(window, "<Control-c>"))
    editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=paste)
    # Creation of help functions
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", underline=0, command=helpme)
    helpmenu.add_separator()
    helpmenu.add_command(label="About...", underline=0, command=about)
    # Addition of menus on menu bar
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # Creation of text space
    textarea = Text(window, wrap='word', undo=TRUE)
    textarea.config(state='normal')
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
    textarea.bind("<Control-a>",select_all)
    textarea.bind("<Control-A>",select_all)
    textarea.bind("<Control-v>",paste)
    textarea.bind("<Control-V>",paste)
    # Open window
    window.config(menu=menubar)
    window.geometry("1000x800")
    window.mainloop()


# Test Example:
initialize_texteditor()
