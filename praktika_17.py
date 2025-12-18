from tkinter import *

tern = "X"
wins_x = 0
wins_o = 0
game_over = False

def check_win():
    global wins_x, wins_o, game_over

    lines = [
        (btn[0], btn[1], btn[2]), (btn[3], btn[4], btn[5]), (btn[6], btn[7], btn[8]),
        (btn[0], btn[3], btn[6]), (btn[1], btn[4], btn[7]), (btn[2], btn[5], btn[8]),
        (btn[0], btn[4], btn[8]), (btn[2], btn[4], btn[6])
    ]
    for a, b, c in lines:
        if a['text'] == b['text'] == c['text'] != '-':
            winner = a['text']
            lbl.configure(text=winner + " победил, молодец")
            if winner == "X":
                wins_x += 1
            else:
                wins_o += 1
            score_lbl.configure(text=f"X: {wins_x}   O: {wins_o}")
            game_over = True
            return
    # Ничья
    if all(b['text'] != '-' for b in btn):
        lbl.configure(text="ничья, эх")
        game_over = True

def clicked(i):
    global tern, game_over
    if game_over or btn[i]['text'] != '-':
        return
    btn[i].configure(text=tern)
    if tern == "X":
        tern = "0"
    else:
        tern = "X"
    check_win()

def restart():
    global tern, game_over
    tern = "X"
    game_over = False
    lbl.configure(text='')
    for b in btn:
        b.configure(text='-')
    score_lbl.configure(text=f"X: {wins_x}   O: {wins_o}")


window = Tk()
window.title("tip and toe")
window.geometry("1000x1000")

lbl = Label(window, text='', font=('Arial Bold', 50))
lbl.grid(column=0, row=0, columnspan=4)

score_lbl = Label(window, text="X: 0   O: 0", font=('Arial Bold', 30))
score_lbl.grid(column=0, row=4, columnspan=4)

restart_btn = Button(window, text="по новой", font=('Arial Bold', 20), command=restart)
restart_btn.grid(column=0, row=5, columnspan=4)

btn = [
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=0: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=1: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=2: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=3: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=4: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=5: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=6: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=7: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=8: clicked(i))
]

btn[0].grid(column=1, row=1)
btn[1].grid(column=2, row=1)
btn[2].grid(column=3, row=1)
btn[3].grid(column=1, row=2)
btn[4].grid(column=2, row=2)
btn[5].grid(column=3, row=2)
btn[6].grid(column=1, row=3)
btn[7].grid(column=2, row=3)
btn[8].grid(column=3, row=3)

window.mainloop()

# лямбда это такая штука - благодаря которой можно сделать ненадолго безымянную функцию
