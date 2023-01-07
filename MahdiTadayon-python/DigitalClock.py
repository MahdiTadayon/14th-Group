import turtle 
import time 

# turtles----------------------------------------------
turt_frame = turtle.Turtle()
turt_sec = turtle.Turtle()
turt_min = turtle.Turtle()
turt_hour = turtle.Turtle()
# turtle_setting---------------------------------------
def turtle_setting(turt, color, pensize):
    turt.hideturtle()
    turt.speed(0)
    turt.pen(pencolor=color, pensize=pensize)

turtle_setting(turt_frame, 'black', 5)
turtle_setting(turt_sec, 'red', 1)
turtle_setting(turt_min, 'green', 1)
turtle_setting(turt_hour, 'blue', 1)

def up_setpos_down(turt, x, y):
    turt.up()
    turt.setpos(x, y)
    turt.down()
# turtleFrame------------------------------------------
up_setpos_down(turt_frame, -25, 5)
turt_frame.write('|',font=('Arial' , 40, 'normal'))
up_setpos_down(turt_frame,50,5)
turt_frame.write('|',font=('Arial' , 40, 'normal'))
up_setpos_down(turt_frame, -90, 60)

turt_frame.forward(220)
turt_frame.right(90)
turt_frame.forward(60)
turt_frame.right(90)
turt_frame.forward(220)
turt_frame.right(90)
turt_frame.forward(60)
turt_frame.up()
# localTime--------------------------------------------
localTime = time.localtime()
tm_sec = localTime.tm_sec
tm_min = localTime.tm_min
tm_hour = localTime.tm_hour
#------------------------------------------------------
def writeTime(turt,tm,x,y):
    up_setpos_down(turt,x,y)
    if tm > 9 :
        turt.write(tm,font=('Arial' , 40, 'normal'))
    else :
        turt.write('0{}'.format(tm),font=('Arial' , 40, 'normal'))
# main-------------------------------------------------
writeTime(turt_sec, tm_sec, 65, 0)
writeTime(turt_min, tm_min, -10, 0)
writeTime(turt_hour, tm_hour, -85, 0)
while(True) :
    if(tm_sec == 60) :
        tm_sec = 0
        turt_min.clear()
        tm_min += 1
        writeTime(turt_min, tm_min, -10, 0)
    if(tm_min == 60) :
        tm_min = 0
        turt_hour.clear()
        tm_hour += 1
        writeTime(turt_hour, tm_hour, -85, 0)
    if(tm_hour == 24):
        tm_hour = 0 
    
    writeTime(turt_sec, tm_sec, 65, 0)
    tm_sec += 1   
    time.sleep(1)
    turt_sec.clear()
    
