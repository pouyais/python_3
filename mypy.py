from tkinter import *
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('first project')
root.config(bg = 'yellow')
# ====== func ==============
x = 20
x1 = 190
def gain_size() :
    global x
    x += 1
    lbl_wel.config(font= f'arial {x} bold')
    

def lessen_size():
    global x
    x -= 1
    lbl_wel.config(font= f'arial {x} bold')
def right():
    global x1
    x1 += 10
    lbl_wel.place(x = x1, y= 100)

def left():
    pass




# ========= label ========
lbl_wel = Label(root,text= 'welcome',fg= 'red',font=f'arial {x} bold' , bg= 'yellow')
lbl_wel.place(x= x1,y= 100)

# ====== button =========
btn_plus = Button(root,text = '+' ,font= 'arial 20',command= gain_size )
btn_plus.place(x= 50,y= 200)
btn_r = Button(root,text = '->' ,font= 'arial 20',command= right )
btn_r.place(x= 100,y= 200)
btn_l = Button(root,text = '<-' ,font= 'arial 20',command= left )
btn_l.place(x= 360,y= 200)

btn_negetive = Button(root,text= '-',font= 'arial 20',command= lessen_size)
btn_negetive.place(x=420,y=200)
print('***********')

root.mainloop()