from tkinter import *
import math

# Constants

PINK = "#e2979c"
RED = "E7305b"
GREEN = "9bdeac"
YELLOW = "f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
repetitions = 0

# Timer Reset


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title_label.config(text="Pomodoro")
    check_mark.config(text="")
    start_button.config(state="normal")
    global repetitions
    repetitions = 0


# Time Mechanism


def start_timer():
    global repetitions
    repetitions += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    start_button.config(state="disabled")

    if repetitions == 0 or repetitions % 2 != 0:
        title_label.config(text="Work", fg="white", font=(FONT_NAME, 35, "bold"), bg="gray")
        count_down(work_time)

    elif repetitions % 2 == 0 and repetitions != 0 and repetitions != 8:
        title_label.config(text="Break", fg="white", font=(FONT_NAME, 35, "bold"), bg="gray")
        count_down(short_break_time)

    elif repetitions == 8:
        title_label.config(text="Long Break", fg="white", font=(FONT_NAME, 35, "bold"), bg="gray")
        count_down(long_break_time)


# Countdown Mechanism


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        marks = ""
        work_sessions = math.floor(repetitions/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)
        if repetitions != 8:
            start_button.config(state="normal")


# UI Setup


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="gray")

title_label = Label(text="Pomodoro", fg="white", font=(FONT_NAME, 35, "bold"), bg="gray")
check_mark = Label(text="", fg="green", bg="gray", font=35)
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)

canvas = Canvas(width=200, height=224, bg="gray", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
tomato_projection = canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
frame = Frame(window, borderwidth=5, relief="ridge", width=200, height=100)


canvas.grid(column=1, row=1)
start_button.grid(column=0, row=4)
reset_button.grid(column=2, row=4)
title_label.grid(column=1, row=0)
check_mark.grid(column=1, row=5)


window.mainloop()
