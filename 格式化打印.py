# #-*- coding :utf-8 -*-

#格式化打印
name = input('name:')
age = input('age:')
job = input('job:')
salary = input('工资：')

msg = '''
--------info of %s---------#这里的每个%s就是一个占位符，本行的代表后面括号里的name
姓名 = %s
年龄 = %s
工作 = %s
工资 = %s
''' % (name, name, age, job, salary)

print(msg*2)#打印2遍
