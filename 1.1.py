from turtle import *
import os
import time

def clear():
    os.system('cls')


def load():
    print("请稍等，正在加载引用文件：")
    time.sleep(0.25)
    p = 0
    for i in range(100):
        print(p,"%")
        time.sleep(0.01)
        clear()
        p += 1
    clear()
    penup()
    goto(-50,-500)
    pendown()

def drawPolygon():
    print("加载完成，正在绘制……")
    time.sleep(3)
    if color == "red":
        pencolor("red")
    elif color == "blue":
        pencolor("blue")
    else:
        pencolor("black")
    for i in range(n):
        if n > 10:
            fd(20)
        else:
            fd(200)
        lt(360/n)
    clear()
    print("绘制完成")
    time.sleep(1)

def drawCircle(n):
    print("加载完成，正在绘制……")
    time.sleep(3)
    if color == "red":
        pencolor("red")
    elif color == "blue":
        pencolor("blue")
    else:
        pencolor("black")
    circle(n)
    clear()
    print("绘制完成")
    time.sleep(1)

speed(0)
tracer(0)
clear()
while True:
    clearscreen()
    clear()
    sh = str(input('''
-------------------欢迎使用画图 version:1.1------------------
请输入你想画的图形（circle or polygon）
circle:圆形
polygon:多边形
'''))
    if sh == "polygon":
        clear()
        n = int(input("输入角的数量："))
        clear()
        color = str(input("请输入颜色，有红色、蓝色和黑色："))
        clear()
        load()
        drawPolygon()
        
    elif sh == "circle":
        clear()
        n = int(input("输入半径："))
        clear()
        color = str(input("请输入颜色，有红色、蓝色和黑色："))
        clear()
        load()
        drawCircle(n)

    clear()
    c = str(input("请问是否继续作图？"))
    if c == "yes":
        pass
    else:
        break
    
