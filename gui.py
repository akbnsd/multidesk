import tkinter as tk
root = tk.Tk()
root.geometry('1500x750')
root.title('Multidesk')

def btn1_screen():
    btn1_frame = tk.Frame(main_frame)
    
    lb = tk.Label(btn1_frame, text='Successfully accessed PC No. 1', font=('bold', 30))
    lb.pack()
    
    btn1_frame.pack(pady=20)
    
def btn2_screen():
    btn2_frame = tk.Frame(main_frame)
    
    lb = tk.Label(btn2_frame, text='Successfully accessed PC No. 2', font=('bold', 30))
    lb.pack()
    btn2_frame.pack(pady=20)
    
def btn3_screen():
    btn3_frame = tk.Frame(main_frame)
    
    lb = tk.Label(btn3_frame, text='Successfully accessed PC No. 3', font=('bold', 30))
    lb.pack()
    
    btn3_frame.pack(pady=20)
    
def btn4_screen():
    btn4_frame = tk.Frame(main_frame)
    
    lb = tk.Label(btn4_frame, text='Successfully accessed PC No. 4', font=('bold', 30))
    lb.pack()
    
    btn4_frame.pack(pady=20)


def hide_indicators():
    btn1_indicate.config(bg='#c3c9cc')
    btn2_indicate.config(bg='#c3c9cc')
    btn3_indicate.config(bg='#c3c9cc')
    btn4_indicate.config(bg='#c3c9cc')
    
def delete_screen():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicator(lb, page):
    hide_indicators()
    lb.config(bg='black')
    delete_screen()
    page()

options_frame = tk.Frame(root, bg='#c3c9cc')

btn1 = tk.Button(options_frame, text='PC No. 1', font=('bold', 15), fg='black', bd=0, bg='#c3c9cc', command=lambda: indicator(btn1_indicate, btn1_screen()))
btn1.place(x=50, y=50)
btn1_indicate = tk.Label(options_frame, text=' ', bg='#c3c9cc')
btn1_indicate.place(x=50, y=51, width=3, height=36)

btn2 = tk.Button(options_frame, text='PC No. 2', font=('bold', 15), fg='black', bd=0, bg='#c3c9cc', command=lambda: indicator(btn2_indicate, btn2_screen()))
btn2.place(x=50, y=200)
btn2_indicate = tk.Label(options_frame, text=' ', bg='#c3c9cc')
btn2_indicate.place(x=50, y=201, width=3, height=36)


btn3 = tk.Button(options_frame, text='PC No. 3', font=('bold', 15), fg='black', bd=0, bg='#c3c9cc', command=lambda: indicator(btn3_indicate, btn3_screen()))
btn3.place(x=50, y=350)
btn3_indicate = tk.Label(options_frame, text=' ', bg='#c3c9cc')
btn3_indicate.place(x=50, y=351, width=3, height=36)


btn4 = tk.Button(options_frame, text='PC No. 4', font=('bold', 15), fg='black', bd=0, bg='#c3c9cc', command=lambda: indicator(btn4_indicate, btn4_screen()))
btn4.place(x=50, y=500)
btn4_indicate = tk.Label(options_frame, text=' ', bg='#c3c9cc')
btn4_indicate.place(x=50, y=501, width=3, height=36)



options_frame.pack(side=tk.LEFT)
options_frame.propagate(False)
options_frame.configure(width=200, height=800)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(pady=50)
main_frame.propagate(False)
main_frame.configure(width=1200, height=700)

root.mainloop()
