from  tkinter import*

root = Tk()

#creating the size of the window.
root.geometry("500x300")

#creating a fun
def getvals():
    print("Accept")

#creating the header
Label(root, text="Sign In", font="tr 15 bold").grid(row=0, column=3)

#creating the field name
email = Label(root, text="Email")
password = Label(root, text="Password")

#displaying/packing the fields in the window
email.grid(row=3, column=2)
password.grid(row=4, column=2)

#creating a variable to store the values.
emailvalue  = StringVar
passwordvalue = StringVar
checkvalue = IntVar

#creating the entry field 
emailentry = Entry(root, textvariable=emailvalue)
passwordentry = Entry(root, textvariable=passwordvalue)

#displaying/packing the entry fields
emailentry.grid(row=3, column=3)
passwordentry.grid(row=4, column=3)

#creating a checkbox
checkbtn = Checkbutton(text="remember me", variable=checkvalue)
checkbtn.grid(row=5, column=3)

#creating a button
Button(text="SUBMIT", command=getvals).grid(row=6,column=3)

root.mainloop()


