# #-*- coding :utf-8 -*-
#
# #格式化打印
# name = input('name:')
# age = int(input('age:'))
# print(type(age))
# job = input('job:')
# salary = input('工资：')
#
# msg = '''
# --------info of %s---------
# 姓名 = %s
# 年龄 = %d
# 工作 = %s
# 工资 = %s
# ''' % (name, name, age, job, salary)
#
# print(msg*2)#打印2遍


n = 1
while n <= 3:
    score = int(input('输入分数：'))
    if score >= 90:
        print('优秀')
    elif score < 90 and score >= 80:
        print('良好')
    elif score >= 60 and score < 80:
        print('及格')
    else:
        print('不及格')
    n += 1

    if n == 4:
        choose_confirm = input('是否需要继续：若要继续请输入“y”，按其他推出')
        if choose_confirm == 'y':
           n = 1

# MSG = '我是%s,年龄%d,目前学习进度为%d%%'%('季方超',35,10)
# print (MSG)
