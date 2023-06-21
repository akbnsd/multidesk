import tkinter as tk
from tkinter import *


root = None
host_listbox = None
openStreamingWindow = lambda a : a

def renderGui():
    global root, host_listbox
    # root = Tk()
    # root.title("Multidesk")

    
    # # Create the host host_listbox
    # host_listbox = Listbox(root)
    # host_listbox.pack(side=LEFT, fill=BOTH, expand=True)

    # # Create the scrollbar for the host host_listbox
    # scrollbar = Scrollbar(root)
    # scrollbar.pack(side=RIGHT, fill=Y)

    # # Configure the scrollbar for the host host_listbox
    # host_listbox.config(yscrollcommand=scrollbar.set)
    # scrollbar.config(command=host_listbox.yview)
        
    # # Create the connect button
    # connect_button = Button(root, text="Connect", command=openStreamingWindow)
    # connect_button.pack(side=BOTTOM, padx=10, pady=10)
    # root.mainloop()
    
    
    
    root = Tk()
    root.title('Multidesk')
    # root.geometry("500x700")
    Frame(root).columnconfigure(tuple(range(60)), weight=1)
    Frame(root).rowconfigure(tuple(range(30)), weight=1)

    ip_var=StringVar()

    scrollbar = Scrollbar(root)
    # scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.grid(column=2, row=0, rowspan=2, sticky='ns')
    
    host_listbox = Listbox(root, yscrollcommand=scrollbar.set, bg="#f0f0f0", font=('calibre',10, 'italic'), border=2, relief="solid")

    # host_listbox.pack(side=LEFT,anchor = N, fill=Y)
    host_listbox.grid(column=0, row=0, columnspan=2, sticky='we')
    # host_listbox.config(width=50, height=30)
    scrollbar.config(command=host_listbox.yview)

    ip_entry = Entry(root,textvariable = ip_var, font=('calibre',10,'normal'))
    # ip_entry.pack(side=LEFT,anchor=CENTER, padx=70)
    ip_entry.grid(column=0, row=1)
    # ip_entry.config(width=31)
    sub_btn=Button(root,text = 'Connect', command = openStreamingWindow, fg='black',font=('Bold', 10))
    # sub_btn.pack(side=LEFT, anchor=CENTER)
    sub_btn.grid(column=1, row=1)
    


    # main_frame = Frame(root, highlightbackground='black', highlightthickness=2)
    # main_frame.pack(pady=50)
    # main_frame.propagate(False)
    # main_frame.configure(width=1200, height=700)

    statusvar = StringVar()
    statusvar.set("Ready")
    sbar = Label(root, textvariable=statusvar, relief = SUNKEN)
    # sbar.pack(side=BOTTOM, fill=X)

    root.mainloop()

