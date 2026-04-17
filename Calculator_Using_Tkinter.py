# GUI- Create A Calculator Using Tkinter

from tkinter import *

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update() 
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

#-------------------------Creating the GUI------------------#
# Setting up the geometry and title of the window
root.geometry("400x700")
root.title("Calculator")
root.configure(bg="#1e1e1e")



#-------------------------Display------------------#
#Asking for the user input and showing it on the screen using Entry Widget
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font= "lucida 40 bold",bg="#2d2d2d",fg="white",bd=0,justify=RIGHT)

screen.pack(fill=X, ipadx=8,pady=10,padx=10)


#-------------------------Buttons Function------------------#
# Creating a frame to hold the buttons
f = Frame(root, bg="grey")

# First Row- 7,8,9
b = Button(f, text="9",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "9", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10)  # Packing the button to the left side of the frame with padding

b = Button(f, text="8",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "8", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

b = Button(f, text="7",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "7", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

f.pack()

# Second Row- 4,5,6
f = Frame(root, bg="grey")

b = Button(f, text="6",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "9", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10)  # Packing the button to the left side of the frame with padding

b = Button(f, text="5",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "8", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

b = Button(f, text="4",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "7", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

f.pack()


f = Frame(root, bg="grey")

# Third Row- 1,2,3
b = Button(f, text="3",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "9", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10)  # Packing the button to the left side of the frame with padding

b = Button(f, text="2",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "8", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

b = Button(f, text="1",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "7", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

f.pack()

f = Frame(root, bg="grey")

# First Row- 0,-,*
b = Button(f, text="*",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "9", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10)  # Packing the button to the left side of the frame with padding

b = Button(f, text="-",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "8", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

b = Button(f, text="0",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "7", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

f.pack()

f = Frame(root, bg="grey")

# First Row- /,=,C
b = Button(f, text="/",padx= 10,pady= 10,font= "Lucida 35 bold") # Creating a button with text "9", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10)  # Packing the button to the left side of the frame with padding

b = Button(f, text="=",padx= 10,pady= 10,font= "Lucida 35 bold",bg="#ff9500" ) # Creating a button with text "8", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

b = Button(f, text="C",padx= 10,pady= 10,font= "Lucida 35 bold",bg="#ff3b30") # Creating a button with text "7", padding and font
b.bind("<Button-1>",click) # Binding the button to the click function
b.pack(side = LEFT,padx=10,pady=10) # Packing the button to the left side of the frame with padding

f.pack()


root.mainloop()
