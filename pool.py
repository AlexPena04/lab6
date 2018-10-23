from graphics import *
import time

WIDTH = 600
HEIGHT = 400
RADIUS = 25
DX = 3
DY = 3
SPEED = 1/20

def main():
    global DX, DY
    win = GraphWin('Pool Table', WIDTH, HEIGHT)
    win.setBackground('yellow')
    ball = Circle(Point(WIDTH/2, HEIGHT/2), RADIUS)
    ball.setFill('red')
    ball.draw(win)
    win.getMouse()
    for i in range(65):
        ball.move(DX,DY)
        time.sleep(SPEED)
        center = ball.getCenter()
        current_x = center.getX()
        current_y = center.getY()
    if current_x > WIDTH - RADIUS:
        DX = -1
    if current_x < 0:
        DX = -1
    if current_y > HEIGHT - RADIUS:
        DY = -1
    if current_y < 0:
        DY= -1

    win.getMouse()
    win.close()
       
main()
