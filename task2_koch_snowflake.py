import turtle

def koch(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch(t, length, level - 1)
        t.left(60)
        koch(t, length, level - 1)
        t.right(120)
        koch(t, length, level - 1)
        t.left(60)
        koch(t, length, level - 1)

def snowflake(t, length, level):
    for _ in range(3):
        koch(t, length, level)
        t.right(120)

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 3-5): "))
    length = 300

    screen = turtle.Screen()
    screen.title("Фрактал Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()

    snowflake(t, length, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
