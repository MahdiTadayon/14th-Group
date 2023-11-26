import turtle
import time
current_time = time.localtime(time.time())
temp_hour = current_time.tm_hour
temp_min = current_time.tm_min
temp_sec = current_time.tm_sec
# Solution 1
while True:
    turtle.hideturtle()
    turtle.clear()
    # turtle.clear()
    turtle.write(f'{str(temp_hour).zfill(2)}:{str(temp_min).zfill(2)}:{str(temp_sec).zfill(2)}',
                 move=False, align='center', font=('Arial narrow', 50, 'normal'))
    time.sleep(1)
    temp_sec += 1
    if temp_sec == 60:
        temp_sec = 0
        temp_min += 1
    if temp_min == 60:
        temp_min = 0
        temp_hour += 1
    if temp_hour == 13:
        temp_hour = 1

# Solution 2
turtle.hideturtle()
while True:
    current_time = time.localtime(time.time())
    turtle.write('{:02}:{:02}:{:02}'.format(current_time.tm_hour, current_time.tm_min, current_time.tm_sec),
                 move=False, align='center', font=('Arial narrow', 50, 'normal'))
    time.sleep(1.1)
    turtle.clear()
