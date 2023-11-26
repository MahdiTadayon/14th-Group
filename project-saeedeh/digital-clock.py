import time
import datetime
import turtle

window = turtle.Turtle()
t = turtle.Turtle()  # create rectangle box
t.pensize(5)
t.hideturtle()
t.setpos(-50, 0)
for i in range(2):
    t.fd(300)
    t.left(90)
    t.fd(70)
    t.left(90)
myTime = time.localtime()    # obtain current hour, minute and second
second = myTime.tm_sec
minute = myTime.tm_min
hour = myTime.tm_hour

while True:
    window.hideturtle()
    window.clear()
    window.write(str(hour).zfill(2) + ":" +
                 str(minute).zfill(2) + ":" +
                 str(second).zfill(2), font=("Arial", 35, "bold"))
    time.sleep(1)
    second += 1

    if second == 60:
        second = 0
        minute += 1

    if minute == 60:
        minute = 0
        hour += 1

    if hour == 13:
        hour = 1

