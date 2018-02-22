from turtle import *

digits = input("Please enter an integer less than 10,000 greater than 0:  ")

mode("logo")   # resets turtle heading to north
speed(0)
ht()
fd(100)

def one():
    pu()
    goto(0, 100)
    seth(90)
    pd()
    fd(35)

def two():
    pu()
    goto(0, 65)
    seth(90)
    pd()
    fd(35)

def three():
    pu()
    goto(0, 100)
    seth(135)
    pd()
    fd(50)

def four():
    pu()
    goto(0, 65)
    seth(45)
    pd()
    fd(50)

def five():
    pu()
    goto(0, 100)
    seth(90)
    pd()
    fd(35)
    rt(135)
    fd(50)

def six():
    pu()
    goto(30, 100)
    seth(180)
    pd()
    fd(35)

def seven():
    pu()
    goto(0, 100)
    seth(90)
    pd()
    fd(35)
    rt(90)
    fd(35)

def eight():
    pu()
    goto(0, 65)
    seth(90)
    pd()
    fd(35)
    lt(90)
    fd(35)

def nine():
    pu()
    goto(0, 100)
    seth(90)
    pd()
    fd(35)
    rt(90)
    fd(35)
    rt(90)
    fd(35)

def ten():
    pu()
    goto(0, 100)
    seth(-90)
    pd()
    fd(35)

def twenty():
    pu()
    goto(0, 65)
    seth(-90)
    pd()
    fd(35)

def thirty():
    pu()
    goto(0, 100)
    seth(-135)
    pd()
    fd(50)

def forty():
    pu()
    goto(0, 65)
    seth(-45)
    pd()
    fd(50)

def fifty():
    pu()
    goto(0, 100)
    seth(-90)
    pd()
    fd(35)
    lt(135)
    fd(50)

def sixty():
    pu()
    goto(-30, 100)
    seth(180)
    pd()
    fd(35)

def seventy():
    pu()
    goto(0, 100)
    seth(-90)
    pd()
    fd(35)
    lt(90)
    fd(35)

def eighty():
    pu()
    goto(0, 65)
    seth(-90)
    pd()
    fd(35)
    rt(90)
    fd(35)

def ninety():
    pu()
    goto(0, 100)
    seth(-90)
    pd()
    fd(35)
    lt(90)
    fd(35)
    lt(90)
    fd(35)

def oneHundred():
    pu()
    goto(0, 0)
    seth(90)
    pd()
    fd(35)

def twoHundred():
    pu()
    goto(0, 35)
    seth(90)
    pd()
    fd(35)

def threeHundred():
    pu()
    goto(0, 0)
    seth(45)
    pd()
    fd(50)

def fourHundred():
    pu()
    goto(0, 35)
    seth(135)
    pd()
    fd(50)

def fiveHundred():
    pu()
    goto(0, 0)
    seth(90)
    pd()
    fd(35)
    lt(135)
    fd(50)

def sixHundred():
    pu()
    goto(30, 0)
    seth(0)
    pd()
    fd(35)

def sevenHundred():
    pu()
    goto(0, 0)
    seth(90)
    pd()
    fd(35)
    lt(90)
    fd(35)

def eightHundred():
    pu()
    goto(0, 35)
    seth(90)
    pd()
    fd(35)
    rt(90)
    fd(35)

def nineHundred():
    pu()
    goto(0, 0)
    seth(90)
    pd()
    fd(35)
    lt(90)
    fd(35)
    lt(90)
    fd(35)

def oneThousand():
    pu()
    goto(0, 0)
    seth(-90)
    pd()
    fd(35)

def twoThousand():
    pu()
    goto(0, 35)
    seth(-90)
    pd()
    fd(35)

def threeThousand():
    pu()
    goto(0, 0)
    seth(-35)
    pd()
    fd(50)

def fourThousand():
    pu()
    goto(0, 35)
    seth(-135)
    pd()
    fd(50)

def fiveThousand():
    pu()
    goto(0, 0)
    seth(-90)
    pd()
    fd(35)
    rt(135)
    fd(50)

def sixThousand():
    pu()
    goto(-30, 0)
    seth(0)
    pd()
    fd(35)

def sevenThousand():
    pu()
    goto(0, 0)
    seth(-90)
    pd()
    fd(35)
    rt(90)
    fd(35)

def eightThousand():
    pu()
    goto(0, 35)
    seth(-90)
    pd()
    fd(35)
    lt(90)
    fd(35)

def nineThousand():
    pu()
    goto(0, 0)
    seth(-90)
    pd()
    fd(35)
    rt(90)
    fd(35)
    rt(90)
    fd(35)

if digits[-1] == "1":
    one()

if digits[-1] == "2":
    two()

if digits[-1] == "3":
    three()

if digits[-1] == "4":
    four()

if digits[-1] == "5":
    five()

if digits[-1] == "6":
    six()

if digits[-1] == "7":
    seven()

if digits[-1] == "8":
    eight()

if digits[-1] == "9":
    nine()

if digits[-2:-1] == "1":
    ten()

if digits[-2:-1] == "2":
    twenty()

if digits[-2:-1] == "3":
    thirty()

if digits[-2:-1] == "4":
    forty()

if digits[-2:-1] == "5":
    fifty()

if digits[-2:-1] == "6":
    sixty()

if digits[-2:-1] == "7":
    seventy()

if digits[-2:-1] == "8":
    eighty()

if digits[-2:-1] == "9":
    ninety()

if digits[-3:-2] == "1":
    oneHundred()

if digits[-3:-2] == "2":
    twoHundred()

if digits[-3:-2] == "3":
    threeHundred()

if digits[-3:-2] == "4":
    fourHundred()

if digits[-3:-2] == "5":
    fiveHundred()

if digits[-3:-2] == "6":
    sixHundred()

if digits[-3:-2] == "7":
    sevenHundred()

if digits[-3:-2] == "8":
    eightHundred()

if digits[-3:-2] == "9":
    nineHundred()

if digits[-4:-3] == "1":
    oneThousand()

if digits[-4:-3] == "2":
    twoThousand()

if digits[-4:-3] == "3":
    threeThousand()

if digits[-4:-3] == "4":
    fourThousand()

if digits[-4:-3] == "5":
    fiveThousand()

if digits[-4:-3] == "6":
    sixThousand()

if digits[-4:-3] == "7":
    sevenThousand()

if digits[-4:-3] == "8":
    eightThousand()

if digits[-4:-3] == "9":
    nineThousand()

    
