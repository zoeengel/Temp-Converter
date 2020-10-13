# NAME: ZOE ANNASTASIA ENGEL
# CLASS: 1
# DATE: 13-10-2020

from tkinter import *

# CREATING THE WINDOW
page=Tk()
page.geometry("500x500")
page.title("Temperature Converter")
page.config(bg="brown")

#CLEAR BUTTON FUNCTION
def clear_function():
    c_f_value.delete(0,END)
    lblResult1.configure(text="")
    f_c_value.delete(0,END)
    lblResult2.configure(text="")

# EXIT BUTTON FUNCTION
def exit_function():
    raise SystemExit
    sys.exit()

# DISPLAYING A HEADING IN MY WINDOW
description = Label(text="Temperature Converter Application" ,fg = "red", relief="solid", font=("Sans-Serif",18, "bold"))
description.pack()

# DEFINING FUNCTIONS
def tocel():
    fahr=(f_c_value.get())

    answer1=((float(fahr)-32) * 5.0 / 9.0)
    lblResult2.configure(text=answer1)

def tofahr():
   celcius=float(c_f_value.get())
   answer2= celcius * 9.0 / 5.0 + 32
   lblResult1.configure(text=answer2)


#CELSIUS TO FAHRENHEIT LABEL AND ENTRY
c_f=Label(page, text="Enter temperature in Celsius: ", font="Ariel",)
c_f.pack(padx=15, pady=20)
c_f_value=Entry(page, width=20, bg="linen")
c_f_value.pack()
lblResult1= Label(page, text="", width=20)
lblResult1.pack()

# CELSIUS ACTIVATION BUTTON
#CButton=Button(page, text="Activate Celsius > Fahrenheit", bg="lime", command=tocel)
#CButton.pack(pady=20, padx=20)

Convertbtn1=Button(page, text="Celsius > Fahrenheit", bg="linen",command=tofahr )
Convertbtn1.pack(pady=20, padx=20)

# FAHRENHEIT TO CELSUIS LABEL AND ENTRY
f_c=Label(page, text="Enter temperature in Fahrenheit: ", font="Ariel")
f_c.pack(padx=15, pady=20)
f_c_value=Entry(page, width=20, bg="linen")
f_c_value.pack()
lblResult2= Label(page, text="", width=20)
lblResult2.pack()

# FAHRENHEIT ACTIVATION BUTTON
#FButton=Button(page, text="Activate Fahrenheit > Celsius", bg="lime")
#FButton.pack(pady=20, padx=20)

#CONVERT BUTTON
Convertbtn=Button(page, text="Fahrenheit > Celsius", bg="linen", command=tocel, )
Convertbtn.pack(pady=20, padx=20)

#CLEAR BUTTON
CB=Button(page, text="Clear", command = clear_function)
CB.pack()


EB=Button(page, text="Exit", command=exit_function)
EB.pack()
page.mainloop()
