import tkinter

window = tkinter.Tk()
window.title("My first Gui program")
window.minsize(height=300, width=500)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()


window.mainloop()
