from tkinter import  *


window = Tk()
window.title("Guess The Number Game")
window.configure(bg="#0b1220")   # dark background
window.geometry("600x500")


welcome = Frame(window, bg = "black")
welcome.pack(fill="both", expand=True)

top_spacer = Frame(welcome, bg="black")
top_spacer.pack(fill="both", expand=True)

label1 = Label(welcome, text = "Welcome to guessing game!",
            bg = "black",
            fg = "#4cc9ff",
            font = ("Arial", 25, "bold"))
label1.pack()

label2 = Label(welcome, text = "Press start button",
            bg = "black",
            fg = "#bdebff",
            font = ("Arial", 15, "bold"))
label2.pack()

def start():
    welcome.pack_forget()
    title_frame.pack(fill = "x")
    label3.pack()

button = Button(welcome, text = "start", font = ("Arial", 20),
                bg = "#1C4D8D",
                 fg = "white" ,
                 command = start)
button.pack()
bottom_spacer = Frame(welcome, bg="black")
bottom_spacer.pack(fill="both", expand=True)







# main container
title_frame = Frame(window, bg="#0b1220")



# main text layer
label = Label(
    title_frame,
    text="Guess any number!",
    font= ("Arial", 25, "bold"),
    fg="#4cc9ff",   
    bg="#0b1220")
label.pack()


label3 = Label(title_frame, 
            bg = "#BDE8F5", fg = "black",
            font = ("Arial", 15),
            height = 2, width = 15)
label3.pack()


button2 = Button(title_frame , text = "check", 
                 bg = "#79C9C5",
                 fg = "white")

button2.pack(pady  = 10)















window.mainloop()
