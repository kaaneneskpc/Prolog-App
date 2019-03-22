from tkinter import *
import json
import backend

def get_selected_row(event):
    try:
        index = list1.curselection()[0]
        global selected_tuple
        selected_tuple = list1.get(index)
        json_acceptable_string = selected_tuple.replace("'", "\"")
        global d
        d = json.loads(json_acceptable_string)
        #print(type(d),"<-this")
        e1.delete(0,END)
        e1.insert(END,d['Title'])
        e2.delete(0, END)
        e2.insert(END,d['Director'])
        e3.delete(0, END)
        e3.insert(END,d['Year'])
        e4.delete(0, END)
        e4.insert(END,d['Rate'])
        e5.delete(0, END)
        e5.insert(END,d['Genre'])
        e6.delete(0, END)
        e6.insert(END,d['Actor'])
    except IndexError:
        pass                #listbox bos ise bisey yapma

def view_command():
    list1.delete(0, END)  # temizle
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), genre_text.get(), rate_text.get(), actor_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), genre_text.get(), rate_text.get(), actor_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), genre_text.get(), rate_text.get(), actor_text.get()))

def delete_command():
    backend.delete(d)
    view_command()

def update_command():
    backend.update(d,title_text.get(), author_text.get(), year_text.get(), genre_text.get(), rate_text.get(), actor_text.get())
    view_command()

#GUI
window = Tk()
window.wm_title("The Movie Store")
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Director")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "IMDB Rate")
l4.grid(row = 1, column = 2)
#
l5 = Label(window, text = "Genre")
l5.grid(row = 2, column = 0)

l6 = Label(window, text = "Actor")
l6.grid(row = 2, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

rate_text = StringVar()
e4 = Entry(window, textvariable = rate_text)
e4.grid(row = 1, column = 3)

genre_text = StringVar()
e5 = Entry(window, textvariable = genre_text)
e5.grid(row = 2, column = 1)

actor_text = StringVar()
e6 = Entry(window, textvariable = actor_text)
e6.grid(row = 2, column = 3)


list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 3, column =0, rowspan = 6, columnspan = 2)

list1.bind('<<ListboxSelect>>',get_selected_row)


sb1 = Scrollbar(window)
sb1.grid(row = 3, column = 2, rowspan = 6)
list1.config(yscrollcommand = sb1.set)
sb1.config(command = list1.yview)

b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 3, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 4, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row = 5, column = 3)

b4 = Button(window, text = "Update selected", width = 12, command = update_command)
b4.grid(row = 6, column = 3)

b5 = Button(window, text = "Delete selected", width = 12, command = delete_command)
b5.grid(row = 7, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 8, column = 3)
window.mainloop()