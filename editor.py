from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import os
from datetime import datetime, time
import keyboard


texti = 0
imgi = 0
textboxi = 0
font = 10
global selected
selected = False


class Window(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master
                self.init_window()

                #canvas
                '''
                self.x=1
                self.y=0
                self.canvas=Canvas(master)
                self.rectangle = self.canvas.create_rectangle(
                         5, 5, 25, 25, fill = "black")
                self.canvas.pack()
 
                # calling class's movement method to
                # move the rectangle
                self.movement()
        def movement(self):
 
                # This is where the move() method is called
                # This moves the rectangle to x, y coordinates
                self.canvas.move(self.rectangle, self.x, self.y)
 
                self.canvas.after(100, self.movement)

        # for motion in negative x direction
        def left(self, event):
                print(event.keysym)
                self.x = -5
                self.y = 0
     
        # for motion in positive x direction
        def right(self, event):
                print(event.keysym)
                self.x = 5
                self.y = 0
     
        # for motion in positive y direction
        def up(self, event):
                print(event.keysym)
                self.x = 0
                self.y = -5
     
        # for motion in negative y direction
        def down(self, event):
                print(event.keysym)
                self.x = 0
                self.y = 5


                '''
                #//

        def init_window(self):
                self.theme = "white"
                global textboxi, font
                self.textbox = Text(self.master, undo=True,font=("Helvetica", font))
                self.textbox.pack(fill=BOTH, expand=1)
                textboxi = 1

                self.master.title("Editor Gui")
                self.pack()

                global menu
                menu = Menu(self.master)
                self.master.config(menu=menu)

                #set variable for open file name
                global open_status_name
                open_status_name=False

                # File button in the ribbon

                file = Menu(menu)
                file.add_command(label="New File", command=self.new_file)
                file.add_command(label="Open File",command=self.open_file)
                file.add_command(label="Open Folder",command=self.open_dir)
                file.add_command(label="Save",command=self.save_file)
                file.add_command(label="Save As...",command=self.save_as_file)
                file.add_command(label="Close File", command=self.close_file)
                file.add_command(label="Close Folder",command=self.close_dir)
                file.add_command(label="Exit", command=self.clientexit,accelerator="Ctrl+Q")

                menu.add_cascade(label="File", menu=file)

                # Edit button in the ribbon

                edit = Menu(menu)
                edit.add_command(label="Delete", command=self.delete_element)
                edit.add_command(label="Undo", command=self.textbox.edit_undo)
                edit.add_command(label="Redo", command=self.textbox.edit_redo)
                edit.add_command(label="Cut", command=self.cut_text)
                edit.add_command(label="Copy", command=self.copy_text)
                edit.add_command(label="Paste", command=self.paste_text)
                edit.add_command(label="Select All", command=self.select_all)
                edit.add_command(label="Find", command=self.openfind)
                edit.add_command(label="Find and replace",command=self.openfind)
                edit.add_command(label="Time/Date",command=self.time)
                edit.add_command(label="Insert Image",command=self.print_img)

                menu.add_cascade(label="Edit", menu=edit)

                # View button in the ribbon
                view = Menu(menu)

                view.add_command(label="Enter Full Screen",command=self.fullscreen)
                view.add_command(label="Hide Menu",command=self.hide_menu)

                menu.add_cascade(label="View", menu=view)

                # Preferences button in the ribbon

                preferences = Menu(menu)

                preferences.add_command(label="Theme", command=self.change_theme)
                preferences.add_command(label="Font +", command=self.font_up)
                preferences.add_command(label="Font -", command=self.font_down)

                menu.add_cascade(label="Preferneces", menu=preferences)

        def new_file(self):
                root2 = Toplevel()
                root2.geometry("400x300")
                app2 = Window(root2)
                global open_status_name
                open_status_name=False


        def open_file(self):
                
                #delete text
                self.textbox.delete("1.0",END)

                #grab filename
                text_file=filedialog.askopenfilename(initialdir="./",title="Open file",filetypes=(("text files","*.txt"),("html files","*.html"),("python files","*.py"),("all files","*.*")))
                self.master.title(text_file)

                #check to see if there is a file name
                if text_file:
                        #make file name global so we can access it later
                        global open_status_name
                        open_status_name=text_file

                        #open the file
                        text_file=open(text_file, "r")
                        stuff=text_file.read()

                        #add file to textbox
                        self.textbox.insert(END,stuff)
                        #close the opened file
                        text_file.close()

        
        def save_as_file(self):
                text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="./",title="Save file",filetypes=(("text files","*.txt"),("html files","*.html"),("python files","*.py"),("all files","*.*")))
                if text_file:
                        global open_status_name
                        open_status_name=text_file

                        name=text_file
                        self.master.title(name)
                        
                        #save file
                        text_file=open(text_file,"w")
                        text_file.write(self.textbox.get(1.0,END))
                        #close file
                        text_file.close()
                        messagebox.showinfo(f"Saved as {name}")
        
        def save_file(self):
                global open_status_name
                if open_status_name:
                        #save file
                        text_file=open(open_status_name,"w")
                        text_file.write(self.textbox.get(1.0,END))
                        #close file
                        text_file.close()
                        messagebox.showinfo("Saved")
                else:
                        #save_as_file()
                        text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="./",title="Save file",filetypes=(("text files","*.txt"),("html files","*.html"),("python files","*.py"),("all files","*.*")))
                        if text_file:
                                name=text_file
                                self.master.title(name)
                        
                                #save file
                                text_file=open(text_file,"w")
                                text_file.write(self.textbox.get(1.0,END))
                                #close file
                                text_file.close()
                                messagebox.showinfo(f"Saved as {name}")

        def open_dir(self):
                folder=filedialog.askdirectory(initialdir=os.path.normpath("C://"),title="Example")
                self.master.title(folder)

                #check to see if there is a file name
                if folder:
                        global frame
                        frame=Toplevel()
                        frame.geometry("200x200")
                        
                        #frame=Frame(root)
                        myList = os.listdir(folder)
                        #print(myList)

                        #position=self.textbox.index(INSERT)
                        #self.textbox.insert(position,myList)
                        #myListBox.delete(0, END)
                        myListBox = Listbox(frame)

                        for file in myList:
                                myListBox.insert(END, file)
                        myListBox.pack()
        


        def print_img(self):

                #define canvas
                my_canvas = Canvas(root, width=1000, height=1000, bg="blue")
                my_canvas.pack(fill="both",expand=True)

                global img,image_file
                #file image
                image_file = filedialog.askopenfilename(title="select your image", filetypes= [("image files",".png"),("image files",'.jpg')])
                img = ImageTk.PhotoImage(Image.open(image_file))
        
                #canvas image
                my_image = my_canvas.create_image(100, 100, anchor=NW, image=img)

                

                def move(e):
                        #e.x
                        #e.y
                        global img,image_file
                        if(True):
                                
                                img = ImageTk.PhotoImage(Image.open(image_file))
                                my_canvas.delete()
                                my_image=my_canvas.create_image(e.x,e.y,image=img)

                                my_label.config(text="Coordonates: x "+str(e.x)+ " y "+str(e.y))

                
                def resizer(ev):
                        global img1,resized,new_img
                        #e.width
                        #e.height
                        global img,image_file
                        #open our image
                        img1 = Image.open(image_file)
                        canvas1=my_canvas
                        #resize the image
                        resized=img1.resize((ev.width,ev.height),Image.ANTIALIAS)
                        #define our image
                        new_img=ImageTk.PhotoImage(resized)
                        #add it back to the canvas
                        my_canvas.create_image(100,100,anchor=NW,image=new_img)
                
                

                my_label=Label(root,text="")
                my_label.pack(pady=20)

                my_canvas.bind('<B1-Motion>',move)
                #my_canvas.bind('<Configure>',resizer)
                

        def close_dir(self):
                global frame
                #folder=filedialog.askdirectory(initialdir=os.path.normpath("C://"),title="Example")
                self.master.title("Editor Gui")
                frame.destroy()

        def close_file(self):
                self.master.destroy()

        def clientexit(self):
                exit()

        def delete_element(self):
                self.textbox.delete('1.0', END)

        def fullscreen(self):
                self.master.state("zoomed")

        def font_up(self):
                global font
                font = font + 1
                if textboxi:
                        self.textbox.config(font=("Helvetica", font))

        def font_down(self):
                global font
                font = font - 1
                if textboxi:
                        self.textbox.config(font=("Helvetica", font))

        def change_theme(self):
                if self.theme == "white":
                        self.configure(bg="black")
                        self.textbox.config(fg="white", bg="black")
                        self.theme = "black"
                elif self.theme == "black":
                        self.configure(bg="white")
                        self.textbox.config(fg="black", bg="white")
                        self.theme = "white"

        # edit
        def cut_text(self):
            global selected
            if self.textbox.selection_get():
                selected = self.textbox.selection_get()
                self.textbox.delete("sel.first", "sel.last")

        def copy_text(self):
            global selected
            if self.textbox.selection_get():
                selected = self.textbox.selection_get()

        def paste_text(self):
            if selected:
                position = self.textbox.index(INSERT)
                self.textbox.insert(position, selected)

        def select_all(self):
            self.textbox.tag_add(SEL, '1.0', END)
            self.textbox.mark_set(INSERT, "1.0")
            self.textbox.see(INSERT)
            return 'break'

        def openfind(self):
                '''
                windowfind = tk.Toplevel(app)
                windowfind.geometry("400x500+600+200")
                windowfind.configure(bg="#FFFFFF")
                windowfind.resizable(True, True)
                img=ImageTk.PhotoImage(Image.open("./images/youwin.jpg"))
                windowfind.title("find")
                '''
                root = Tk()
                # root window is the parent window
                fram = Frame(root)

                # Creating Label, Entry Box, Button
                # and packing them adding label to
                # search box
                Label(fram, text='Find').pack(side=LEFT)

                # adding of single line text box
                edit = Entry(fram)

                # positioning of text box
                edit.pack(side=LEFT, fill=BOTH, expand=1)

                # setting focus
                edit.focus_set()

                # adding of search button
                Find = Button(fram, text='Find')
                Find.pack(side=LEFT)

                Label(fram, text="Replace With ").pack(side=LEFT)

                edit2 = Entry(fram)
                edit2.pack(side=LEFT, fill=BOTH, expand=1)
                edit2.focus_set()

                replace = Button(fram, text='FindNReplace')
                replace.pack(side=LEFT)

                fram.pack(side=TOP)

                
                def find():

                        # remove tag 'found' from index 1 to END
                        self.textbox.tag_remove('found', '1.0', END)
     
                        # returns to widget currently in focus
                        s = edit.get()
     
                        if (s):
                                idx = '1.0'
                                while 1:
                                        # searches for desired string from index 1
                                        idx = self.textbox.search(s, idx, nocase = 1,
                                                stopindex = END)
             
                                        if not idx: break
             
                                        # last index sum of current index and
                                        # length of text
                                        lastidx = '% s+% dc' % (idx, len(s))
             
 
                                        # overwrite 'Found' at idx
                                        self.textbox.tag_add('found', idx, lastidx)
                                        idx = lastidx
 
                                        # mark located string as red
         
                                        self.textbox.tag_config('found', foreground ='red')
                                edit.focus_set()
                
                def findNreplace():
     
                        # remove tag 'found' from index 1 to END
                        self.textbox.tag_remove('found', '1.0', END)
     
                        # returns to widget currently in focus
                        s = edit.get()
                        r = edit2.get()
     
                        if (s and r):
                                idx = '1.0'
                                while 1:
                                        # searches for desired string from index 1
                                        idx = self.textbox.search(s, idx, nocase = 1,
                                                stopindex = END)
                                        print(idx)
                                        if not idx: break
             
                                        # last index sum of current index and
                                        # length of text
                                        lastidx = '% s+% dc' % (idx, len(s))
 
                                        self.textbox.delete(idx, lastidx)
                                        self.textbox.insert(idx, r)
 
                                        lastidx = '% s+% dc' % (idx, len(r))
             
                                        # overwrite 'Found' at idx
                                        self.textbox.tag_add('found', idx, lastidx)
                                        idx = lastidx
 
                                # mark located string
                                self.textbox.tag_config('found', foreground ='white', background = 'blue')
                        edit.focus_set()


                Find.config(command=find)
                replace.config(command=findNreplace)

                root.mainloop()
        
        def time(self):
                print(os.times)
                # datetime object containing current date and time
                now = datetime.now()
                print("now =", now)

                # dd/mm/YY H:M:S
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("date and time =", dt_string)

                position=self.textbox.index(INSERT)
                self.textbox.insert(position,dt_string)

        #view
        global enabled
        enabled=True

        def show_menu():
                print("gata")
                root.config(menu = menu)
 
        def hide_menu(self):

                global enabled
                enabled=False
                '''
                global enabled
                if enabled:
                        enabled = False
                        menu.entryconfigure(2,state=tk.DISABLED)
                else:
                        enabled = True
                        menu.entryconfigure(2,state=tk.NORMAL)
                '''
                emptyMenu = Menu(root)
                root.config(menu=emptyMenu)
                messagebox.showinfo("show menu-Ctrl+q               ")

                '''
                if keyboard.read_key() == "q":
                        print("You pressed q")
                        #show_menu()
                        root.config(menu = menu)
                '''

                #root.config(menu = Menu(self.master))
                #show_menu()     
        
        
        #if(enabled==False):
           #     root.bind("<Control-x>",show_menu)

        

root = Tk()
root.geometry("400x300")

app = Window(root)
app.mainloop()



