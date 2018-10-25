# 使用while循环输入 1 2 3 4 5 6     8 9 10
while True:
    number = int(input('请输入一个数字:'))
    if number > 10:
        break
    elif number == 7:
        continue
    print(number)
