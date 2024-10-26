money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month_spend = 0 # Прожитые месяцы без долгов

while True:
    money_capital += salary
    money_capital -= spend

    if money_capital < 0: # Условие, когда мы залезли в долги
        break

    month_spend += 1
    spend += spend * increase #Повышение цен

print("Количество месяцев, которое можно протянуть без долгов:", month_spend)
