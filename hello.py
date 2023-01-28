def greeting_function(name, age):
    print('Welcome '+name+".You are " +str(age)+ ' years old.')

name = input('Enter your name: ')
age = input('Enter you age: ')
greeting_function(name, age)