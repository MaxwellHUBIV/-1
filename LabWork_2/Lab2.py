salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_pillow = 0 # Подушка безопасноти, которую нужно расчитать

for _ in range(months):
    money_pillow += spend - salary
    spend += spend * increase # повышение цен

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_pillow))
