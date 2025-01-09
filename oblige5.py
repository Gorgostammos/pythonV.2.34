import tkinter as tk

calculation = ""


def skrive_number(symbol):
    global calculation
    calculation += str(symbol)
    resultat.delete(1.0, tk.END)
    resultat.insert(1.0, calculation)

def el_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))

        resultat.delete(1.0, tk.END)
        resultat.insert(1.0, calculation)
    except:
        clear_field()
        resultat.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    resultat.delete(1.0, tk.END)


window = tk.Tk()
window.geometry("250x250")
window.title("oblig 5 calc")


resultat = tk.Text(height=2, width=17, font=("Arial", 24))
resultat.grid(columnspan=5)

btn1 = tk.Button(text="1", command=lambda: skrive_number(1), width=3, font=("Bold", 12))
btn1.grid(row=2, column=1)

btn2 = tk.Button(text="2", command=lambda: skrive_number(2), width=3, font=("Bold", 12))
btn2.grid(row=2, column=2)

btn3 = tk.Button(text="3", command=lambda: skrive_number(3), width=3, font=("Bold", 12))
btn3.grid(row=2, column=3)

btn4 = tk.Button(text="4", command=lambda: skrive_number(4), width=3, font=("Bold", 12))
btn4.grid(row=3, column=1)

btn5 = tk.Button(text="5", command=lambda: skrive_number(5), width=3, font=("Bold", 12))
btn5.grid(row=3, column=2)

btn6 = tk.Button(text="6", command=lambda: skrive_number(6), width=3, font=("Bold", 12))
btn6.grid(row=3, column=3)

btn7 = tk.Button(text="7", command=lambda: skrive_number(7), width=3, font=("Bold", 12))
btn7.grid(row=4, column=1)

btn8 = tk.Button(text="8", command=lambda: skrive_number(8), width=3, font=("Bold", 12))
btn8.grid(row=4, column=2)

btn9 = tk.Button(text="9", command=lambda: skrive_number(9), width=3, font=("Bold", 12))
btn9.grid(row=4, column=3)

btn0 = tk.Button(text="0", command=lambda: skrive_number(0), width=3, font=("Bold", 12))
btn0.grid(row=5, column=1)


btn_pluss = tk.Button(text="+", command=lambda: skrive_number("+"), width=3, font=("Bold", 12))
btn_pluss.grid(row=5, column=4)

btn_dele = tk.Button(text=":", command=lambda: skrive_number("/"), width=3, font=("Bold", 12))
btn_dele.grid(row=4, column=4)

btn_minus = tk.Button(text="-", command=lambda: skrive_number("-"), width=3, font=("Bold", 12))
btn_minus.grid(row=5, column=3)

btn_gange = tk.Button(text="x", command=lambda: skrive_number("*"), width=3, font=("Bold", 12))
btn_gange.grid(row=3, column=4)

btn_alik = tk.Button(text="=", command=el_calculation, width=3,  font=("Bold", 12), fg="#ff7c17")
btn_alik.grid(row=5, column=2)


btn_selt = tk.Button(text="Delet", command= clear_field, width=3, font=("Bold", 12), fg="#ff7c17")
btn_selt.grid(row=2, column=4)









window.mainloop()

