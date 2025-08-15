from tkinter import *

# Create main window
root = Tk()
root.title("My Calculator")
root.geometry('510x580')
root.configure(bg="#1deee3")  # Light background

# Fonts
font = ('Verdana', 22, 'bold')
header_font = ('Algerian', 26, 'bold')
entry_font = ('Arial', 20)

# Heading Label with background color
heading = Label(root, text='My Calculator', font=header_font,
                bg="#3ef918", fg="white", pady=10)
heading.pack(side=TOP, fill=X)

# Text field for input/output
textFeild = Entry(root, font=entry_font, justify=CENTER,
                  bd=5, relief=RIDGE, bg="#eef2f3", fg="#333")
textFeild.pack(side=TOP, pady=20, fill=X, padx=20)

# Button click handler
def on_click(event):
    button_text = event.widget["text"]

    if button_text == "=":
        try:
            expression = textFeild.get()
            result = eval(expression)
            textFeild.delete(0, END)
            textFeild.insert(END, str(result))
        except:
            textFeild.delete(0, END)
            textFeild.insert(END, "Error")

    elif button_text == "AC":
        textFeild.delete(0, END)

    elif button_text == "<--":
        current_text = textFeild.get()
        textFeild.delete(0, END)
        textFeild.insert(0, current_text[:-1])

    elif button_text == "X":
        textFeild.insert(END, "*")  # Replace X with *
    
    else:
        textFeild.insert(END, button_text)

# Common button style
btn_style = {
    "font": font,
    "width": 5,
    "relief": RIDGE,
    "bg": "#ffffff",
    "fg": "#222222",
    "activebackground": "#fdd522",
    "activeforeground": "white",
    "bd": 2
}

# Button Frame
buttonFrame = Frame(root, bg="#3ef918")
buttonFrame.pack(side=TOP, padx=10)

# Numeric Buttons (1–9)
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), **btn_style)
        btn.grid(row=i, column=j, padx=5, pady=5)
        btn.bind('<Button-1>', on_click)
        temp += 1

# Row 4 buttons (0 . =)
btn_texts = ['0', '.', '=']
for index, text in enumerate(btn_texts):
    btn = Button(buttonFrame, text=text, **btn_style)
    btn.grid(row=3, column=index, padx=5, pady=5)
    btn.bind('<Button-1>', on_click)

# Operators
operators = ['+', '-', 'X', '/']
for index, op in enumerate(operators):
    btn = Button(buttonFrame, text=op, **btn_style)
    btn.grid(row=index, column=3, padx=5, pady=5)
    btn.bind('<Button-1>', on_click)

# Clear & All Clear
clearbtn = Button(buttonFrame, text="<--", font=font, width=11,
                  bg="#e6c327", fg="white", activebackground="#da9e07",
                  activeforeground="white", relief=RIDGE)
clearbtn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
clearbtn.bind('<Button-1>', on_click)

allclearbtn = Button(buttonFrame, text="AC", font=font, width=11,
                     bg="#ec2e18", fg="white", activebackground="#b11b0a",
                     activeforeground="white", relief=RIDGE)
allclearbtn.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
allclearbtn.bind('<Button-1>', on_click)

# Run the app
root.mainloop()