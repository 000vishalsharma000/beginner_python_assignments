import turtle
import math

len = int(input("enter the distance  of vertex  from centre of pentagon"))
area_d = 5*(1/2)*(len**2)*math.sin(72)

print("area of penatgon is : ", area_d, "\n")

lenth = int(input("enter the length of side  of pentagon"))
area_s = (((5)*(lenth**2))/(4*(math.tan(36))))

print("area of penatgon is : ", area_s, "\n")

num = 1234


def reverse_num(num):
    r_num = 0
    while num != 0:
        last_dig = num % 10
        num //= 10
        r_num *= 10
        r_num += last_dig
    return r_num


print("reverse of ", num, " is ", reverse_num(1234), " \n ")

r = int(input("enter radius to draw olympic sign"))


turtle.pensize(8)

turtle.color('blue')
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(r)

turtle.color('black')
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(r)

turtle.color('red')
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(r)

turtle.color('yellow')
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(r)

turtle.color('green')
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(r)
