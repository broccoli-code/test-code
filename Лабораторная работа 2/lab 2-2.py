money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

def calculate_months_without_debt(money_capital, salary, spend, increase):
    months = 0

    while True:
        if months > 0:
            spend *= (1 + increase)

        budget = salary + money_capital
        if budget < spend:
            break

        money_capital -= max(0, spend - salary)
        months += 1

    return months

months_without_debt = calculate_months_without_debt(money_capital, salary, spend, increase)

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt)
