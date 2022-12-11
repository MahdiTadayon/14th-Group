# import turtle
#
#
# from datetime import datetime
#
# # current dateTime
# now = datetime.now()
#
# # convert to string
# date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
# print('DateTime String:', date_time_str)
#
# date_time_str = now.strftime("%H:%M:%S")
# print('DateTime String:', date_time_str)

import time
import datetime as dte
import turtle

# Creating a turtle for displaying time
tt1 = turtle.Turtle()

# Creating the screen
screen = turtle.Screen()
# Setting the background color for the screen
screen.bgcolor("pink")


while True:
    tt1.hideturtle()
    tt1.clear()
    now = dte.datetime.now()
    # Displaying the generated time
    tt1.write(now.strftime("%H:%M:%S"),
              font=("Bnazanin", 40, "bold"))
    time.sleep(1)




# secs = dte.datetime.now().second
# mins = dte.datetime.now().minute
# hrs = dte.datetime.now().hour
#
# while True:
#     tt1.hideturtle()
#     tt1.clear()
#     # Displaying the generated time
#     tt1.write(str(hrs).zfill(2)
#               + ":" + str(mins).zfill(2) + ":"
#               + str(secs).zfill(2),
#               font=("Callibri Narrow", 37, "bold"))
#     time.sleep(1)
#     secs += 1
#     if secs == 60:
#         secs = 0
#         mins += 1
#     if mins == 60:
#         mins = 0
#         hrs += 1
#     if hrs == 13:
#         hrs = 1
#
