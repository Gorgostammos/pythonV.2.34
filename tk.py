import tkinter as tk
import tk_helper as tkh


def save_game(game_list, listbox_game, ent_game_name, etn_game_year, ent_game_age):
    name = ent_game_name.get()
    year = int(etn_game_year.get())
    age = int(ent_game_age.get())

    key = f'{name} ({year})'
    game_list[key] = {'name': name, 'year': year, 'age': age}
    listbox_game.insert(tk.END, key)

def info_game2(game_list2, listbox_game, ent_game_name, etn_game_year, ent_game_age):
    name = ent_game_name.get()
    year = int(etn_game_year.get())
    age = int(ent_game_age.get())

    key = f'{name} was released in {year} and you have to be {age} to play'
    game_list2[key] = {'name': name, 'year': year, 'age': age}
    listbox_game.insert(tk.END, key)




def game_selected(game_list, listbox_game, ent_game_name, etn_game_year, ent_game_age):
    this_game = listbox_game.curselection()
    print(this_game)
    if this_game:
        global this_game_is
        game_id = listbox_game.get(listbox_game.curselection())
        game = game_list[game_id]
        this_game_is.set(game['name'])
        etn_game_year.delete(0, tk.END)
        ent_game_age.delete(0, tk.END)
        etn_game_year.insert(0, game['year'])
        ent_game_age.insert(0, game['age'])


def clear_game_from_list(*entries):
    ent_game_name.delete(0, tk.END)
    etn_game_year.delete(0, tk.END)
    ent_game_age.delete(0, tk.END)

    for entry in entries:
        entry.delete(0, tk.END)


def delete_game(game_list, listbox_game):
    this_game = listbox_game.curselection()
    print(this_game)
    if this_game:
        game_id = listbox_game.get(this_game)
        game_list.pop(game_id)
        listbox_game.delete(listbox_game.curselection())
        clear_game_from_list()

        top = tk.Toplevel()
        top.attributes("-topmost", True)
        top.title('Movie Deleted')
        tk.Label(top, text=f" {game_id} now is deleted ").pack()
        tk.Button(top, text="OK", command=top.destroy).pack(padx=100)

#her prøvde jeg å lage en knapp som skulle gi hele info om spillet som ble valgt
#def info_game(game_list, listbox_game):
#    games.get(listbox_game.curselection())
#    listbox_game.get(listbox_game.curselection())
#    print(listbox_game)
    #games.get(listbox_game.curselection({f" {}, {'year'} , {'age'}"}))
#    top = tk.Toplevel()
 #   top.attributes("-topmost", True)
 #   top.title('Movie Deleted')
  #  tk.Label(top, text=f"{games.get(listbox_game.curselection(['name']))}").pack()
   # tk.Button(top, text="OK", command=top.destroy).pack(padx=100)


games = {'Spider man 2(2020) ': {'name': 'spider man', 'year': 2020, 'age': 16},
         'Fifa 22(2021) ': {'name': 'Fifa 22', 'year': 2021, 'age': 1}, }


window = tk.Tk()

window.title("oblig 5")
window.geometry("1000x1000")

label = tk.Label(text="Game Register",
                 font=('Arial', 20, 'bold'),
                 fg='#121a19', bg='#5d7371',
                 padx=20, pady=20)
label.pack()


tkh.create_big_ui(25)

main_form = tk.Frame()
left_from = tk.Frame()

this_game_is = tk.StringVar()
ent_game_name = tk.Entry(main_form, textvariable=this_game_is)
etn_game_year = tk.Entry(main_form)
ent_game_age = tk.Entry(main_form)

lbl_game_name = tk.Label(main_form, text="name: ")
lbl_game_year = tk.Label(main_form, text="year: ")
lbl_game_age = tk.Label(main_form, text="age: ")

gameing_list = tk.StringVar(value=list(games.keys()))
listbox_game = tk.Listbox(left_from, listvariable=gameing_list, selectmode=tk.SINGLE)


btn_save = tk.Button(main_form, text="Save", command=lambda: save_game(games, listbox_game, ent_game_name, etn_game_year
                                                                       , ent_game_age))
btn_delete = tk.Button(left_from, text="Delete", command=lambda: delete_game(games, listbox_game))

#btn_info = tk.Button(left_from, text="Info", command=lambda: info_game(games, listbox_game))

lbl_game_name.grid(row=0, column=0, sticky=tk.E)
lbl_game_year.grid(row=1, column=0, sticky=tk.E)
lbl_game_age.grid(row=2, column=0, sticky=tk.E)
ent_game_name.grid(row=0, column=1)
etn_game_year.grid(row=1, column=1)
ent_game_age.grid(row=2, column=1)
btn_save.grid(row=3, column=0, columnspan=2)


listbox_game.pack(fill=tk.BOTH)
btn_delete.pack()

#btn_info.pack()



left_from.pack(side=tk.RIGHT,fill=tk.BOTH, expand=True, pady=10)
main_form.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

listbox_game.bind('<<ListboxSelect>>', lambda event: game_selected(games, listbox_game, ent_game_name, etn_game_year,
                                                                   ent_game_age))

window.mainloop()