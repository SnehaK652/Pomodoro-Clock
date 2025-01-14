from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    Timer_Label.config(text="Timer",fg=GREEN)
    tick_mark_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60


    if reps%8==0:
        count_down(long_break_sec)
        Timer_Label.config(text="Break", fg=RED,font=(FONT_NAME,50,"bold"))
        tick_mark_label.config(text=tick_mark)


    elif reps%(2 )==0 :
        count_down(short_break_sec)
        Timer_Label.config(text="Break",fg=PINK,font=(FONT_NAME,50,"bold"))
        tick_mark_label.config(text=tick_mark)

    else:
        count_down(work_sec)
        Timer_Label.config(text="Work", fg=GREEN,font=(FONT_NAME,50,"bold"))
        tick_mark_label.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min==0:
        count_min="00"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
     global timer
     timer=window.after(1000,count_down,count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=100,pady=50,background=YELLOW)

window.title("Pomodoro")

#fg=GREEN
tick_mark="✔"
Timer_Label=Label(text="Timer",font=(FONT_NAME,50,"bold"),background=YELLOW,fg=GREEN)
Timer_Label.grid(row=1,column=2)

canvas=Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)



Start=Button(text="Start", font=(FONT_NAME, 10, "bold"),highlightthickness=0,background=YELLOW,command=start_timer)
Start.grid(row=3, column=1)


Reset=Button(text="Reset", font=(FONT_NAME, 10, "bold"),highlightthickness=0,background=YELLOW,command=reset_timer)
Reset.grid(row=3, column=3)

tick_mark_label = Label( fg=GREEN, background=YELLOW, highlightthickness=0)
tick_mark_label.grid(row=3, column=2)
tick_mark_label.config(padx=10, pady=10)




window.mainloop()