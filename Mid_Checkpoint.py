from tkinter import *
from tkinter import filedialog
from tkinter import font

root =Tk()
root.title("Mid CheckPoint")
root.geometry("1000x700")


def get(): #Retrieve Button
    myLabel.config(text=my_text.get(1.0, END))

def clear(): #Clear Button
    my_text.delete(1.0, END)
       
def open_text(): #Open text file Button
    text_file=filedialog.askopenfilename(initialdir="c:/", title = 'Open text file', filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file,'r')
    data=text_file.read()

    my_text.insert(END, data)
    text_file.close()

def save_text(): #Saving File
    text_file=filedialog.askopenfilename(initialdir="c:/", title = 'Save text file', filetypes=(("Text Files", "*.txt"),))
    text_file=open(text_file,'w')
    text_file.write(my_text.get(1.0, END))

def select():
    selected_text=my_text.selection_get()
    myLabel.config(text=selected_text)

def bolder():
    bold_font= font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight='bold')

    my_text.tag_configure("bold", font=bold_font)

    current_tags= my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove('bold','sel.first','sel.last')
    else:
        my_text.tag_add('bold','sel.first','sel.last')
                         
def italics():
    italic_font= font.Font(my_text,my_text.cget("font"))
    italic_font.configure(slant='italic')

    my_text.tag_configure("italic", font=italic_font)

    current_tags= my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove('itlaic','sel.first','sel.last')
    else:
        my_text.tag_add('italic','sel.first','sel.last')
                         
def underline():
    underline_font= font.Font(my_text,my_text.cget("font"))
    underline_font.configure(underline=True)

    my_text.tag_configure("underline", font=underline_font)

    current_tags= my_text.tag_names("sel.first")

    if "underline" in current_tags:
        my_text.tag_remove('underline','sel.first','sel.last')
    else:
        my_text.tag_add('underline','sel.first','sel.last')
    

my_text=Text(root, width=60, height=20)
my_text.pack(pady=100)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear Text", command=clear)
clear_button.grid(row=0, column=0, padx=20)

get_text_button = Button(button_frame, text="Retrieve Text", command=get)
get_text_button.grid(row=0, column=1, padx=20)

myLabel= Label(root, text='')
myLabel.pack()

open_text_button = Button(button_frame, text="Open Text File", command=open_text)
open_text_button.grid(row=0, column=2, padx=20)

save_button = Button(button_frame, text='Save Changes', command=save_text)
save_button.grid(row=0,column=4, padx=20)

select_button = Button(button_frame, text='Select Text' , command=select)
select_button.grid(row=0, column=3, padx=20)


bold_button= Button(button_frame, text='Bold', command=bolder)
bold_button.grid(row=1,column=2, padx=20)

italics_button= Button(button_frame, text='Italics', command=italics)
italics_button.grid(row=1,column=3, padx=20)

underline_button= Button(button_frame, text='Underline', command=underline)
underline_button.grid(row=1,column=4, padx=20)

root.mainloop()
