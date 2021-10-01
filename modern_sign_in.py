import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title('Modern Looking Sign In')
root.geometry('650x400+350+220')
#root.resizable(False,False)

# main bg
main_image = tk.PhotoImage(file='bg.png')
img_label = tk.Label(root,image=main_image,borderwidth=0)
img_label.pack()

# Frame on bg
can = tk.Canvas(root)
can.pack()



root.mainloop()