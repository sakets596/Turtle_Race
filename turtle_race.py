import turtle
from time import sleep
from random import randint, choice
from screeninfo import get_monitors

# Getting primary screen's weidth and height
for monitor in get_monitors():
    if monitor.is_primary is True:
        screen_width = monitor.width  # 1728
        screen_mid_width = screen_width / 2
        screen_height = monitor.height  # 1117
        screen_mid_height = screen_height / 2

turtle_count = int(input("How many turtle will participate in race(Max 18) #: "))
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.colormode(255)

turtles = {}
for i in range(turtle_count):
    turtles[f"TUR{i+1}"] = turtle.Turtle()
    turtles[f"TUR{i+1}"].ht()

turtles_dist = {}
for i in range(turtle_count):
    turtles_dist[f"TUR{i+1}_dist"] = 0
    

count = 0
screen_reduce_even = 35
screen_reduce_odd = 35
for tur, tur_obj in turtles.items():
    if count % 2 == 0:
        tur_obj.shape('turtle')
        tur_obj.st()
        tur_obj.color((randint(0,255),randint(0,255),randint(0,255)))
        tur_obj.pu()
        tur_obj.lt(180)
        tur_obj.fd(screen_mid_width - screen_reduce_even)
        tur_obj.rt(90)
        tur_obj.write(f"{tur}", move=False, align="center", font=("Arial", 16, "normal"))
        tur_obj.fd(50)
        screen_reduce_even = screen_reduce_even + 100
        count = count + 1
    else:
        tur_obj.shape('turtle')
        tur_obj.st()
        tur_obj.color((randint(0,255),randint(0,255),randint(0,255)))
        tur_obj.pu()
        tur_obj.fd(screen_mid_width - screen_reduce_odd)
        tur_obj.lt(90)
        tur_obj.write(f"{tur}", move=False, align="center", font=("Arial", 16, "normal"))
        tur_obj.fd(50)
        screen_reduce_odd = screen_reduce_odd + 100
        count = count + 1


def race_finish_line():
    finish_line = turtle.Turtle()
    finish_line.shape('turtle')
    finish_line.pu()
    finish_line.color('red')
    finish_line.fd(screen_mid_width - 10)
    finish_line.lt(90)
    finish_line.fd(screen_mid_height - 100)
    finish_line.lt(90)
    # finish_line.color('red')
    draw_till = screen_width - 10
    count = 1
    while count < draw_till:
        finish_line.pd()
        finish_line.fd(10)
        count = count + 10
        finish_line.pu()
        finish_line.fd(10)
        count = count + 10
    finish_line.ht()


def race_finish_text():
    race_finish = turtle.Turtle()
    race_finish.shape('turtle')
    race_finish.pu()
    race_finish.color('green')
    race_finish.fd(screen_mid_width - 10)
    race_finish.lt(90)
    race_finish.fd(screen_mid_height - 100)
    race_finish.lt(90)
    race_finish.fd(screen_mid_width)
    race_finish.write("FINISH", move=False, align="center", font=("Arial", 16, "normal"))
    race_finish.ht()


def race_start_point():
    start_point_turt = turtle.Turtle()
    start_point_turt.shape('turtle')
    start_point_turt.pu()
    start_point_turt.color('green')
    start_point_turt.fd(screen_mid_width - 10)
    start_point_turt.rt(90)
    start_point_turt.fd(10)
    start_point_turt.rt(90)
    start_point_turt.pd()
    start_point_turt.fd(screen_width - 10)
    start_point_turt.ht()


def score_board():
    score_tur = turtle.Turtle()
    score_tur.shape('turtle')
    score_tur.pu()
    score_tur.color('red')
    score_tur.rt(90)
    score_tur.fd(60)
    score_tur.write("SCORE BOARD", move=False, align="center", font=("Arial", 22, "normal"))
    score_tur.ht()


turtle_list = []
for turt, turt_obj in turtles.items():
    turtle_list.append(turt)

race_start_point()
score_board()
race_finish_line()
race_finish_text()

# start race
sleep(3)

finish_line_value = screen_mid_height - 175

count = 0
fd_steps = 80
while True:
    try:
        tur = choice(turtle_list)
    except IndexError as e:
        print(f"Race Completed !!")
        race_finished = turtle.Turtle()
        race_finished.shape('turtle')
        race_finished.color((14, 171, 56))
        race_finished.rt(90)
        race_finished.pu()
        race_finished.fd(screen_mid_height/2)
        race_finished.write("RACE FINISHED !!", move=False, align="center", font=("Arial", 30, "normal"))
        race_finished.ht()
        input()
        exit()
    tur_obj = turtles[tur]
    fd_value = randint(50, 80)
    tur_obj.fd(fd_value)
    tur_dist = turtles_dist[f"{tur}_dist"] + fd_value
    turtles_dist[f"{tur}_dist"] = tur_dist
    if tur_dist >=  finish_line_value:
        print(f"{tur} finished the race.")
        count = count + 1   
        while count <= 18:
            if count == 1:
                pos = "1ST"
            elif count == 2:
                pos = "2ND"
            elif count == 3:
                pos = "3RD"
            else:
                pos = f"{count}TH"
            position_turtle = turtle.Turtle()
            position_turtle.shape('turtle')
            position_turtle.color('purple')
            position_turtle.rt(90)
            position_turtle.pu()
            fd_steps = fd_steps + 20
            position_turtle.fd(fd_steps)
            position_turtle.rt(90)
            position_turtle.fd(screen_mid_width - 50)
            position_turtle.write(f"{tur}: {pos}", move=False, align="center", font=("Arial", 16, "normal"))
            position_turtle.ht()
            turtle_list.remove(tur)
            break
    sleep(randint(1, 2))
