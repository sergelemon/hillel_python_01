from tkinter import *
import time

def make_ball(event):
    global balls, all_shots
    if all_shots < 10:
        ball = canvas.create_oval(240, 460, 260, 480, fill="gray")
        balls.append(ball)
        all_shots += 1
    info_text()

def info_text():
    global texts
    for text_id in texts:
        canvas.delete(text_id)
    text_id = canvas.create_text(420, 120, text=f'Кількість кораблів: {ship_number+1}')
    texts.append(text_id)
    text_id = canvas.create_text(420, 140, text=f'Кількість вибухiв: {all_shots}')
    texts.append(text_id)
    text_id = canvas.create_text(420, 160, text=f'Кількість попадань: {good_shots}')
    texts.append(text_id)
    if all_shots == 10:
        text_id = canvas.create_text(420, 180, text='Ядра закончились!')
        texts.append(text_id)

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_rectangle(190, 480, 310, 500, fill='black')
canvas.create_rectangle(240, 460, 260, 480, fill='black')
canvas.bind_all('<space>', make_ball)

ship_image = PhotoImage(file="ship.gif")
pow_image = PhotoImage(file="pow.gif")

texts = list()
balls = list()
boom = 0
all_shots = 0
good_shots = 0

for ship_number in range(10):
    canvas.delete(boom)
    boom = 0
    ship = canvas.create_image(500, 0, anchor=NW, image=ship_image)
    info_text()
    for y in range(0, 300):
        if ship != 0:
            canvas.move(ship, -3, 0)
            ship_x = canvas.coords(ship)[0]
        for i in range(len(balls)):
            ball = balls[i]
            if not ball:
                continue
            canvas.move(ball, 0, -5)
            ball_coords = canvas.coords(ball)
            if ship != 0 and ball_coords[1] == 0 and ship_x - 20 <= ball_coords[0] <= ship_x + 100:
                boom = canvas.create_image(ship_x+60, 30, image=pow_image)
                canvas.delete(ship)
                ship = 0
                canvas.delete(ball)
                balls[i] = 0
                good_shots += 1
                info_text()
        tk.update()
        time.sleep(0.02)