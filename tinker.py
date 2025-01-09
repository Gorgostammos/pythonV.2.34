import tkinter as tk


window = tk.Tk()
window.title("Hello tkinter!")

#label
label = tk.Label(text="This is a label!", font=("Arial", 16))
label.pack()

label_2 = tk.Label(text="label 2", font=("Arial", 16), bg="red", fg="white")
label_2.pack()

label_3 = tk.Label(text="label 3 - 0", font=("Arial", 16), bg="yellow", fg="black",
                   height=5, width=10)
label_3.pack()

#knap
button = tk.Button(text ="button!", font=("Times New Roman", 20),
                   bg="black", fg="red",
                   height=2, width=7)
button.pack()

#enter
entry = tk.Entry(font=("Arial", 12), width=15)
entry.pack()

#text
text_box = tk.Text(font=("Arial", 12))
text_box.pack()

window.mainloop()

#print("jojo")