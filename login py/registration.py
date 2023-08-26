from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.config(bg="#fff")
root.resizable(False,False)

def Signin():
    username=user.get()
    password=pword.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Hello Everyone!', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
        screen.mainloop()

    elif username!="admin" and password!="1234":
        messagebox.showerror("invalid", "invalid username and password")

    elif password!="1234":
        messagebox.showerror("invalid", "invalid password")

    elif username!="admin":
        messagebox.showerror("invalid", "invalid username")

##########inserting an Image in the window
img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50,y=50)

frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

##################Creating the username

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')



user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg='black').place(x=25, y=107)
#--------------------------------------------------------------


###################Creating the password
def on_enter(e):
    pword.delete(0, 'end')

def on_leave(e):
    name=pword.get()
    if name=='':
        pword.insert(0, 'Password')

pword = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
pword.place(x=30, y=150)
pword.insert(0,'Password')
pword.bind('<FocusIn>', on_enter)
pword.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg='black').place(x=25, y=177)
#--------------------------------------------------------------


#Creating the Sign in Button 
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,command=Signin).place(x=35, y=204)
label=Label(frame, text="Not Registered Yet?", fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=75, y=270)


sign_up= Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor="hand2", fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()