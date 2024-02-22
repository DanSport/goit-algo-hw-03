import turtle

# Введення рівня рекурсії користувачем
order = int(input("Введіть рівень рекурсії: "))

def koch_snowflake(t, order, size):
    """
    Функція для малювання сніжинки Коха.

    :param t: об'єкт turtle для малювання
    :param order: рівень рекурсії
    :param size: довжина сторони сніжинки
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

# Налаштування Turtle
window = turtle.Screen()
window.bgcolor("lightblue")

t = turtle.Turtle()
t.color("white")
t.speed(0)  # найшвидша швидкість

# Налаштування початкової позиції
t.penup()
t.goto(-150, 90)
t.pendown()

# Малювання сніжинки
for i in range(3):
    koch_snowflake(t, order, 300)
    t.right(120)

turtle.done()
