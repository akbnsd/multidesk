from tkinter import *



root = Tk()
root.geometry("500x500")

photo = PhotoImage(file = "multidesk icon.png")
yash_label = Label(image = photo)
yash_label.pack()
root.title("Multidesk")



frame = Frame(root,bg = "white",borderwidth = 6,relief = SUNKEN )
frame.pack(side =LEFT)








# f2 = Frame(yashkochure_root,bg = "yellow",borderwidth = 25,relief = SUNKEN )
# f2.pack(side = RIGHT,padx = 0 ,pady = 25)
# l2 = Label(f2,text = "Lets go",font = "Arial 25 bold",padx = 200,pady =25)
# l2.pack()
# def hello():
#     print("my name is yashkochure")
    
b1 = Button(frame,text = "Computer 1",fg = "green",bg = "white",font = "Arial 25 bold",)
b1.pack(side = "top",pady = 20,)

b2 = Button(frame,text = "Computer 2",fg = "green",bg = "white",font = "Arial 25 bold")
b2.pack(side = "top",pady = 20)

b3 = Button(frame,text = "Computer 3",fg = "green",bg = "white",font = "Arial 25 bold")
b3.pack(side = "top",pady = 20)

b4 = Button(frame,text = "Computer 4",fg = "green",bg = "white",font = "Arial 25 bold")
b4.pack(side = "top",pady = 20)



# user = Label(root,text = "username")
# password = Label(root,text = "password")
# user.pack()
# password.pack()




# # variable classes in tkinter 
# # BooleanVar,DoubleVar,IntVar,StringVar


# uservalue = StringVar()
# passvalue = StringVar()

# userentry = Entry(root,textvariable = uservalue)
# passentry = Entry(root,textvariable = passvalue)

# userentry.pack()
# passentry.pack()

image_frame = Frame(root, width=900, height=500, bd=1, relief= SOLID)
image_frame.pack()


b5 = Button(root,text = "Connect", bg = "white")
b5.pack()








            











root.mainloop()









