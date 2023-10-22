money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
budget = money_capital + salary
months = 0
while True:
    budget_n = (budget - (spend * pow(1 + increase, months)))
    if budget_n < 0:
        break
    budget = budget_n + salary
    months += 1



print("Количество месяцев, которое можно протянуть без долгов:", months)
