S = 0
n = int(input("Введите количестов билетов"))
vozrast = None
for i in range(1, n + 1):
    vozrast= int(input("Введите возраст посетителя"))
    if 18<= vozrast <25:
        S=S+990
        print("Цена билета 990")
    elif vozrast >= 25:
        S+=1390
        print("Цена билета 1390")
    else:
        print("Билет бесплатный")
if n>3:
    S=S-S//10
    print("Вам положена скидка 10%")
print("У вас", n, "билетов")
print("Общая сумма",S)
