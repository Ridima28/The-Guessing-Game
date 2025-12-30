from tkinter import *

root = Tk()
root.title("My Game")
root.geometry("600x400")


# ---------- welcome (splash) frame ----------
welcome = Frame(root, bg="black")
welcome.pack(fill="both", expand=True)

Label(welcome, text="Welcome to My Game",
      fg="white", bg="black",
      font=("Arial", 24)).pack(pady=40)

def start_game():
    # remove welcome screen
    welcome.pack_forget()

    # show main game frame
    game_frame.pack(fill="both", expand=True)

Button(welcome, text="Start", font=("Arial", 16),
       command=start_game).pack(pady=20)

# ---------- main game frame ----------

game_frame = Frame(root, bg="darkgreen")

Label(game_frame, text="Main Game Screen",
      fg="white", bg="darkgreen",
      font=("Arial", 24)).pack(pady=40)

# start with only welcome visible
root.mainloop()
