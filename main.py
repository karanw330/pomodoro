from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
vari = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(vari)
    timer_txt.config(text='TIMER', fg='green')
    canvas.itemconfig(ms, text=f"25:00")
    check_text.config(text ='')
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, SHORT_BREAK_MIN, LONG_BREAK_MIN, WORK_MIN
    reps += 1
    if reps%2 == 0:
        check_text.config(text = int(reps/2)*'✅')
        if reps%8 == 0:
            timer(LONG_BREAK_MIN*60)
            timer_txt.config(text = 'Long Break', fg = RED )
        else:
            timer(SHORT_BREAK_MIN*60)
            timer_txt.config(text = 'Break', fg=RED)
    else:
        timer(WORK_MIN*60)
        timer_txt.config(text = 'WORK', fg = 'green')



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def timer(count):
    global reps, vari
    seconds = count%60
    minutes = int(count/60)
    if len(str(seconds)) == 1:
        seconds = f"0{seconds}"
    canvas.itemconfig(ms, text = f"{minutes}:{seconds}")
    if count > 0:
        global vari
        vari = window.after(1000, timer, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(background=PINK, padx=50, pady=50)


canvas = Canvas(width=200, height=224, background=PINK, highlightthickness=0)
tomato = PhotoImage(file = 'tomato.png')
canvas.create_image(100, 112, image=tomato)
ms = canvas.create_text(100, 130, text = '25:00', font= (FONT_NAME, 20, 'bold'), fill= 'white')
canvas.grid(column = 1, row = 1)


timer_txt = Label(text = 'TIMER', background=PINK, font=(FONT_NAME, 40), fg= 'green')
timer_txt.grid(column = 1, row = 0)

start_button = Button(text = 'Start', command = start_timer)
start_button.grid(column = 0, row = 3)

reset_button = Button(text = 'Reset', command= reset_timer)
reset_button.grid(column = 2, row = 3)

check_text = Label( bg= PINK, fg=GREEN, font= ('Ariel', 15))
check_text.grid(column = 1, row = 4)

window.mainloop()