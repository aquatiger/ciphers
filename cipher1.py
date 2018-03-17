from turtle import *
import re
import random


# use turtle to draw ciphers of the Cistercian monks

digits = input("Please enter an integer less than 10,000 greater than 0:  ")

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

# ensure input is only digits
p = re.compile(r'^\d+$')
m = p.match(digits)
if m:
    print(digits)
    m = digits
#        digits = input("Please enter an integer less than 10,000 greater than 0:  ")
else:
    print("No match")

colormode(255)
##reddish = random.randrange(255)
##greenish = random.randrange(255)
##bluish = random.randrange(255)
##pencolor(reddish, greenish, bluish)

# pencolor(r, g, b)


mode("logo")   # resets turtle heading to north
pencolor(r, g, b)
pensize(3)
speed(0)
ht()
fd(100)
# pencolor(random.randrange(255), random.randrange(255), random.randrange(255))


# if statements for the ones position
if digits[-1] == "1":
    pu()
    goto(0, 100)
    seth(90)
    pd()
    fd(35)

if digits[-1] == "2":
    pu()
    goto(0, 65)
    seth(90)
    pd()
    fd(35)

if digits[-1] == "3":
    pu()
    goto(0, 100)
    seth(135)
    pd()
    fd(50)

if digits[-1] == "4":
    pu()
    goto(0, 65)
    seth(45)
    pd()
    fd(50)

if digits[-1] == "5":
    pu()
    goto(0, 100)
    seth(90)
    pd()
    fd(35)
    rt(135)
    fd(50)

if digits[-1] == "6":
    pu()
    goto(30, 100)
    seth(180)
    pd()
    fd(35)

if digits[-1] == "7":
    pu()
    goto(0, 100)
    seth(90)
    pd()
    fd(35)
    rt(90)
    fd(35)

if digits[-1] == "8":
    pu()
    goto(0, 65)
    seth(90)
    pd()
    fd(35)
    lt(90)
    fd(35)

if digits[-1] == "9":
    pu()
    goto(0, 100)
    seth(90)
    pd()
    fd(35)
    rt(90)
    fd(35)
    rt(90)
    fd(35)

# if statements for the tens position
if digits[-2:-1] == "1":
    pu()
    goto(0, 100)
    seth(-90)
    pd()
    fd(35)

if digits[-2:-1] == "2":
    pu()
    goto(0, 65)
    seth(-90)
    pd()
    fd(35)

if digits[-2:-1] == "3":
    pu()
    goto(0, 100)
    seth(-135)
    pd()
    fd(50)

if digits[-2:-1] == "4":
    pu()
    goto(0, 65)
    seth(-45)
    pd()
    fd(50)

if digits[-2:-1] == "5":
    pu()
    goto(0, 100)
    seth(-90)
    pd()
    fd(35)
    lt(135)
    fd(50)

if digits[-2:-1] == "6":
    pu()
    goto(-30, 100)
    seth(180)
    pd()
    fd(35)

if digits[-2:-1] == "7":
    pu()
    goto(0, 100)
    seth(-90)
    pd()
    fd(35)
    lt(90)
    fd(35)

if digits[-2:-1] == "8":
    pu()
    goto(0, 65)
    seth(-90)
    pd()
    fd(35)
    rt(90)
    fd(35)

if digits[-2:-1] == "9":
    pu()
    goto(0, 100)
    seth(-90)
    pd()
    fd(35)
    lt(90)
    fd(35)
    lt(90)
    fd(35)

# if statments for the hundreds position
if digits[-3:-2] == "1":
    pu()
    goto(0, 0)
    seth(90)
    pd()
    fd(35)

if digits[-3:-2] == "2":
    pu()
    goto(0, 35)
    seth(90)
    pd()
    fd(35)

if digits[-3:-2] == "3":
    pu()
    goto(0, 0)
    seth(45)
    pd()
    fd(50)

if digits[-3:-2] == "4":
    pu()
    goto(0, 35)
    seth(135)
    pd()
    fd(50)

if digits[-3:-2] == "5":
    pu()
    goto(0, 0)
    seth(90)
    pd()
    fd(35)
    lt(135)
    fd(50)

if digits[-3:-2] == "6":
    pu()
    goto(30, 0)
    seth(0)
    pd()
    fd(35)

if digits[-3:-2] == "7":
    pu()
    goto(0, 0)
    seth(90)
    pd()
    fd(35)
    lt(90)
    fd(35)

if digits[-3:-2] == "8":
    pu()
    goto(0, 35)
    seth(90)
    pd()
    fd(35)
    rt(90)
    fd(35)

if digits[-3:-2] == "9":
    pu()
    goto(0, 0)
    seth(90)
    pd()
    fd(35)
    lt(90)
    fd(35)
    lt(90)
    fd(35)

# if statments for the thousands position
if digits[-4:-3] == "1":
    pu()
    goto(0, 0)
    seth(-90)
    pd()
    fd(35)

if digits[-4:-3] == "2":
    pu()
    goto(0, 35)
    seth(-90)
    pd()
    fd(35)

if digits[-4:-3] == "3":
    pu()
    goto(0, 0)
    seth(-35)
    pd()
    fd(50)

if digits[-4:-3] == "4":
    pu()
    goto(0, 35)
    seth(-135)
    pd()
    fd(50)

if digits[-4:-3] == "5":
    pu()
    goto(0, 0)
    seth(-90)
    pd()
    fd(35)
    rt(135)
    fd(50)

if digits[-4:-3] == "6":
    pu()
    goto(-30, 0)
    seth(0)
    pd()
    fd(35)

if digits[-4:-3] == "7":
    pu()
    goto(0, 0)
    seth(-90)
    pd()
    fd(35)
    rt(90)
    fd(35)

if digits[-4:-3] == "8":
    pu()
    goto(0, 35)
    seth(-90)
    pd()
    fd(35)
    lt(90)
    fd(35)

if digits[-4:-3] == "9":
    pu()
    goto(0, 0)
    seth(-90)
    pd()
    fd(35)
    rt(90)
    fd(35)
    rt(90)
    fd(35)
