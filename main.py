from tkinter import *
import time
import random

x = 20
y = 0
food = []
with open("MySnakeGame\High_Score.txt") as f:
    high_score = f.read()
game = True
game_is_on = True
score = 0
name = ''

window1 = Tk()
window1.title("Welcome")
canvas1 = Canvas(window1, height=window1.winfo_screenheight(), width=window1.winfo_screenwidth())
canvas1.pack(anchor="center")
bg1 = PhotoImage(file="MySnakeGame\Background1.png")
canvas1.create_image(0, 0, image=bg1, anchor="nw")
canvas1.create_text(800, 300, text="WELCOME TO \nSNAKE GAME", font=("Jokerman", 70, "bold"), fill="white")


def start():
    global score
    global bg1
    window1.destroy()
    score = 0
    window2 = Tk()
    window2.title("Name")
    canvas2 = Canvas(window2, height=window2.winfo_screenheight(), width=window2.winfo_screenwidth())
    canvas2.pack(anchor="center")
    bg1 = PhotoImage(file="MySnakeGame\Background1.png")
    canvas2.create_image(0, 0, image=bg1, anchor="nw")
    canvas2.create_text(800, 250, text="ENTER USERNAME", font=("Courier", 40, "bold"), fill="white")
    e = Entry(window2, width=30, font=("Cambria", 20, "italic"))
    e.place(x=590, y=300)
    e.focus_force()

    def click():
        global name
        name = e.get().lower()

    Button(window2, text="GO AHEAD!", background="red", fg="yellow", font=("Courier", 30, "bold"),
           command=lambda: [click(), window2.destroy(), setup()]).place(x=685, y=500)
    window2.mainloop()


def setup():
    game = True
    snake_body = []
    window3 = Tk()
    window3.title("Snake Game")
    window3.focus_force()
    window3.configure(background="dark green")
    canvas3 = Canvas(window3, height=600, width=600, bg="light green", highlightthickness=0)
    canvas3.grid(row=1, columnspan=2)
    oval1 = canvas3.create_oval(140, 285, 170, 315, fill="black", outline="black")
    oval2 = canvas3.create_oval(120, 285, 150, 315, fill="dark green", outline="black")
    oval3 = canvas3.create_oval(100, 285, 130, 315, fill="dark green", outline="black")
    snake_body.append(oval1)
    snake_body.append(oval2)
    snake_body.append(oval3)

    tomato = PhotoImage(file="MySnakeGame\Tomato_image.png")
    for i in range(3):
        p = random.randint(50, 550)
        food.append(canvas3.create_image(p, p, image=tomato, anchor="nw"))

    def left(event):
        global x, y
        if x != 20 and x != -20:
            x = -20
            y = 0

    def right(event):
        global x, y
        if x != -20 and x != 20:
            x = 20
            y = 0

    def up(event):
        global x, y
        if y != 20 and y != -20:
            x = 0
            y = -20

    def down(event):
        global x, y
        if y != -20 and y != 20:
            x = 0
            y = 20

    def scoreboard():
        Label(window3, text=f"Score: {score}", justify="center", bg="red", fg="yellow",
              font=("Arial", 20, "bold"), pady=10, width=17, highlightthickness=0).grid(row=0, column=0)
        Label(window3, text=f"High Score: {high_score}", justify="center", bg="red", fg="yellow",
              font=("Arial", 20, "bold"), pady=10, width=17, highlightthickness=0).grid(row=0, column=1)

    def play(event=0):
        global game
        if game_is_on:
            game = True
            functioning()

    def pause(event=0):
        global game
        if game_is_on:
            game = False

    def play_pause():
        Button(window3, text="PLAY", justify="center", bg="red", fg="yellow", font=("Courier", 20, "bold"), padx=10,
               pady=10, width=16, highlightthickness=0, command=play).grid(row=2, column=0)
        Button(window3, text="PAUSE", justify="center", bg="red", fg="yellow", font=("Courier", 20, "bold"), padx=10,
               pady=10, width=16, highlightthickness=0, command=pause).grid(row=2, column=1)

    scoreboard()
    play_pause()

    window3.bind("<Left>", left)
    window3.bind("<Right>", right)
    window3.bind("<Up>", up)
    window3.bind("<Down>", down)
    window3.bind("<space>", pause)
    window3.bind("<Return>", play)

    def movement():
        for j in range(len(snake_body) - 1, 0, -1):
            c = canvas3.coords(snake_body[j - 1])
            canvas3.moveto(snake_body[j], c[0] - 1, c[1] - 1)
        canvas3.move(snake_body[0], x, y)

    def screen():
        global game
        if canvas3.coords(snake_body[0])[2] > 590 or canvas3.coords(snake_body[0])[0] < 10 or \
                canvas3.coords(snake_body[0])[1] < 10 or canvas3.coords(snake_body[0])[3] > 590:
            game = False
            game_over()

    def collision_food():
        global score
        snake_head_x = sum(canvas3.coords(snake_body[0])[0::2]) / 2
        snake_head_y = sum(canvas3.coords(snake_body[0])[1::2]) / 2
        for k in food:
            food_x = canvas3.coords(k)[0]
            food_y = canvas3.coords(k)[1]
            if -25 < snake_head_x - food_x < 25 and -25 < snake_head_y - food_y < 25:
                x1, y1, x2, y2 = canvas3.coords(snake_body[-1])
                if x == 20:
                    snake_body.append(canvas3.create_oval(x1 - 25, y1, x2 - 25, y2, fill="dark green", outline="black"))
                if x == -20:
                    snake_body.append(canvas3.create_oval(x1 + 25, y1, x2 + 25, y2, fill="dark green", outline="black"))
                if y == 20:
                    snake_body.append(canvas3.create_oval(x1, y1 - 25, x2, y2 - 25, fill="dark green", outline="black"))
                if y == -20:
                    snake_body.append(canvas3.create_oval(x1, y1 + 25, x2, y2 + 25, fill="dark green", outline="black"))
                canvas3.moveto(k, random.randint(50, 550), random.randint(50, 550))
                score += 1
                score_add = canvas3.create_text(300, 50, text="+1", font=("Algerian", 40, "bold"), fill="black")
                window3.after(1000, canvas3.delete, score_add)
                if score % 20 == 0 and score != 0:
                    score += 5
                    score_bonus = canvas3.create_text(300, 100, text="+5 BONUS!", font=("Algerian", 40, "bold"),
                                                      fill="black")
                    window3.after(1000, canvas3.delete, score_bonus)
                scoreboard()

    def collision_tail():
        global game
        snake_head_x = sum(canvas3.coords(snake_body[0])[0::2]) / 2
        snake_head_y = sum(canvas3.coords(snake_body[0])[1::2]) / 2
        for m in range(len(snake_body))[2:]:
            snake_body_x = sum(canvas3.coords(snake_body[m])[0::2]) / 2
            snake_body_y = sum(canvas3.coords(snake_body[m])[1::2]) / 2
            if -15 < snake_head_x - snake_body_x < 15 and -15 < snake_head_y - snake_body_y < 15:
                game = False
                game_over()

    def restart():
        global game_is_on
        global game
        global score
        global x
        global y
        score = 0
        x = 20
        y = 0
        game_is_on = True
        game = True
        window3.destroy()
        setup()

    def close():
        global bg1
        window3.destroy()
        window5 = Tk()
        window5.title("Quit")
        canvas5 = Canvas(window5, height=window5.winfo_screenheight(), width=window5.winfo_screenwidth())
        canvas5.pack(anchor="center")
        bg1 = PhotoImage(file="MySnakeGame\Background1.png")
        canvas5.create_image(0, 0, image=bg1, anchor="nw")
        canvas5.create_text(800, 200, text="THANK YOU!", font=("Courier", 70, "bold"), fill="white")
        canvas5.create_text(800, 400, text="CREATED BY:", font=("Courier", 70, "bold"), fill="white")
        canvas5.create_text(800, 500, text="KEERTHAN SHENOY", font=("Courier", 70, "bold"), fill="white")
        canvas5.create_text(800, 600, text="AMRUTH R", font=("Courier", 70, "bold"), fill="white")
        canvas5.create_text(800, 700, text="C ASHIK POOJARY", font=("Courier", 70, "bold"), fill="white")

    def game_over():
        global high_score
        global game_is_on
        nonlocal snake_body
        global game
        game_is_on = False
        window3.quit()
        window4 = Tk()
        window4.title("Game Over")
        canvas4 = Canvas(window4, height=window4.winfo_screenheight(), width=window4.winfo_screenwidth(),
                         bg="dark blue")
        canvas4.pack(anchor="center")
        canvas4.create_text(800, 200, text="GAME OVER!", font=("Courier", 70, "bold"), fill="red")
        canvas4.create_text(800, 300, text=f"YOUR SCORE: {score}", font=("Courier", 70, "bold"), fill="white")
        Button(window4, text="RESTART", background="red", fg="yellow", font=("Courier", 30, "bold"),
               command=lambda: [window4.destroy(), restart()]).place(x=650, y=550)
        Button(window4, text="QUIT", background="red", fg="yellow", font=("Courier", 30, "bold"),
               command=lambda: [window4.destroy(), close()]).place(x=680, y=650)
        with open("MySnakeGame\High_Score.txt", "w") as file:
            if score > int(high_score):
                high_score = score
                canvas4.create_text(800, 400,
                                    text=f"Congratulations {name.capitalize()}! You have set a new high score",
                                    font=("Cambria", 30, "italic"), fill="black")
            file.write(str(high_score))
        with open("MySnakeGame\\Name.txt", "r") as c:
            name_list = list(map(lambda z: (z.strip()), c.readlines()))
            if name in name_list:
                k = name_list.index(name)
                with open("MySnakeGame\Score_list.txt", "r") as d:
                    score_list = list(map(lambda z: int(z.strip()), d.readlines()))
                    score_list[k] += score
                with open("MySnakeGame\Score_list.txt", "w") as e:
                    for m in score_list:
                        e.write(f"{str(m)}\n")
            else:
                with open("MySnakeGame\\Name.txt", "a") as d:
                    d.write(f"{name}\n")
                with open("MySnakeGame\Score_list.txt", "a") as e:
                    e.write(f"{score}\n")

    def functioning():
        global game
        while game:
            movement()
            screen()
            collision_food()
            collision_tail()
            canvas3.update()
            time.sleep(0.1)

    functioning()
    window3.mainloop()


def instructions():
    window7 = Tk()
    window7.title("Instructions")
    canvas7 = Canvas(window7, height=window7.winfo_screenheight(), width=window7.winfo_screenwidth(), bg="dark blue")
    canvas7.pack()
    canvas7.create_text(800, 150, text="INSTRUCTIONS", font=("Cambria", 70, "italic"), fill="red")
    with open("MySnakeGame\Instructions.txt", "r") as instruct:
        canvas7.create_text(800, 400, text=instruct.read(), font=("Cambria", 30, "italic"), fill="white")
    Button(window7, text="GO BACK", background="red", fg="yellow", font=("Courier", 30, "bold"),
           command=window7.destroy).place(x=700, y=650)


def leaderboard():
    window8 = Tk()
    window8.title("Leaderboard")
    canvas8 = Canvas(window8, height=window8.winfo_screenheight(), width=window8.winfo_screenwidth(), bg="dark blue")
    canvas8.pack()
    canvas8.create_text(750, 100, text="LEADERBOARD", font=("Courier", 70, "bold"), fill="red")
    with open("MySnakeGame\\Name.txt") as a:
        names_list = list(map(lambda st: st.strip(), a.readlines()))
    with open("MySnakeGame\Score_list.txt") as b:
        scores_list = b.readlines()
        scores_list = list(map(lambda st: int(st.strip()), scores_list))
        scores_list_sort = sorted(scores_list, reverse=True)
    space = 200
    for p in scores_list_sort:
        canvas8.create_text(500, space, text=names_list[scores_list.index(p)], font=("Courier", 30, "bold"),
                            fill="white")
        canvas8.create_text(1000, space, text=str(p), font=("Courier", 30, "bold"), fill="white")
        space += 50
    Button(window8, text="GO BACK", background="red", fg="yellow", font=("Courier", 30, "bold"),
           command=window8.destroy).place(x=700, y=650)


Button(window1, text="START", background="red", fg="yellow", font=("Courier", 30, "bold"), command=start).place(y=450,
                                                                                                                x=700)
Button(window1, text="LEADERBOARD", background="red", fg="yellow", font=("Courier", 30, "bold"),
       command=leaderboard).place(y=550, x=620)
Button(window1, text="INSTRUCTIONS", background="red", fg="yellow", font=("Courier", 30, "bold"),
       command=instructions).place(y=650, x=610)
window1.mainloop()
