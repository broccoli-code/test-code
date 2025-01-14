salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

def calculate_money_capital(salary, spend, increase):
    months = 10
    money_capital = 0

    for month in range(months):
        if month > 0:
            spend *= (1 + increase)

        deficit = spend - salary

        if month == 0:
            money_capital += max(0, deficit)
        else:
            money_capital += max(0, deficit)

    return round(money_capital)

required_capital = calculate_money_capital(salary, spend, increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)
