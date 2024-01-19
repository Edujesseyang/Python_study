# -------------------银行倍率计算器--------------------------------
interest = float(input("Enter the interest rate:"))
amount = float(input("How much money do you want to put in:"))
year = int(input("How many years do you want to save: "))

for year in range(year):  # 这里的第一个year和第二个year不一样, 第一个是方程里的临时名字变量, 第二个是用户输入的变量
    print(f'In the year {year}, You have {round(amount, 2)}')
    amount = amount + (amount * interest)
