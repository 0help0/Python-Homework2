f_num = int(input("Введите первое число>>"))
oper = input("Введите операцию>>")
s_num = int(input("Введите второе число>>"))
dalee = 'y'
while dalee == 'y':
    if oper == '+':
        print(f_num + s_num)
    elif oper == '-':
        print(f_num - s_num)
    elif oper == '*':
        print(f_num * s_num)
    elif oper == '/':
        print(f_num / s_num)
    else:
        print("Error")
    dalee = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить>>")