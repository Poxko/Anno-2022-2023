import turtle
t= turtle.Screen()
t = turtle.Turtle()
num = int(input('Inserisci il numero di lati della figura: '))
s=((num-2)*180/num)-180
for i in range(num):
    t.right(s)
    t.forward(100)
